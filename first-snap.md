# Build your first IoT snap

## Creating a CLI application for Ubuntu Core

Snaps are a container technology similar to Docker containers, but they have a number of advantages for edge devices.

* Advanced update features such as automatically healing after a broken update, and ensuring a certain update order.
* Granular secure access from containerized applications to the host system and connected hardware.
* Extensive support for GUI applications.

Ubuntu Core is completely built-up from the ground up from snaps. So to make your application available to Ubuntu core, all you need to do is package it as a snap.

We will try this out with `flaska`, an example Python application that runs a "Hello World" webserver.

The first step is to add a `snapcraft.yaml` file in the repository. This file explains how to build your application, how to package it as a snap, and what permissions the snap requests.

Let's start by adding metadata to `snapcraft.yaml` describing the application.

```yaml
name: flaska
version: '0.1'
summary: Python flask app
description: |
  Example Python Flask app
grade: stable
```

After that, we choose the `base` to use for this snap. This defines two things:

* The Ubuntu version that is used **inside of your application container**. Your application inside of the container will think it is running on that version of Ubuntu, regardless of the host operating system. `core22` is based on Ubuntu 22.04, `core20` is based on Ubuntu 20.04, and so forth. If your app is only compatible with an older version of Ubuntu, you can use that base, and still run your app on newer Ubuntu versions.
* The Ubuntu version used for **building your app**. The build tool starts a container or virtual machine with that version of Ubuntu, regardless of what version of Ubuntu you're currently running. Newer versions of Ubuntu will use newer versions of compilers and build tools. Use the latest version (`core22`), to get the latest build tools.

```yaml
base: core22
```

Next, we define the confinement type. For Ubuntu Core applications, this should always be `strict`. This means that your application runs in a full sandbox, and only has access to the host system if you explicitly grant it. (more on this below)

```yaml
confinement: strict
```

> Regular Linux distributions can use a second type of confinement: `classic`. This means your application has full access to the host system. This is not recommended, however, because it is much harder to make your application work like that, and it is much less secure.

The next step is to define how to build your application. You can split this up into multiple "parts", if your application is composed out of multiple components that need to be built separately. For example, if you have an application with a Java and a Python component, you will need to use at least two parts.

For this application, however, we need only a single part.

```yaml
parts:
  main:
    plugin: python
    source: .
    stage-packages:
      - curl
```

* `plugin` specifies what build tool to use. Take a look at the list of [supported plugins](https://snapcraft.io/docs/supported-plugins) to see what languages are supported.
* `source` explains where to find the source code for this part. This can be a local directory, or it can be remote, such as a GitHub repository, or a zip file to download. We use `.` to specify the sources are in the current directory.
* `stage-packages` describes what additional packages from [the Ubuntu archive](https://packages.ubuntu.com/jammy/allpackages) your application needs. These are the applications you normally install using `apt` in order to get your app to work on Ubuntu.

Finally, we define how to start your application. One snap can have multiple apps inside of it. In this case, we only have a single command: the webserver.

```yaml
apps:
  flaska:
    command: bin/flaska
    plugs: [network-bind]
```

* `command` specifies how to start your application. This is relative from the root of your snap.
* `plugs` specifies what permissions your application wants. `network-bind` means that your application has access to the network and can listen (bind) to a port. Take a look at all the [permissions snap supports](https://snapcraft.io/docs/supported-interfaces).

Note that there is a difference between the permissions that an application _requests_ and the permissions that it actually gets. Getting access is called "connecting an interface to a snap". There are three ways that snaps get connected to interfaces:

* Manual connections: users and device manufacturers can [manually connect and disconnect interfaces](https://snapcraft.io/docs/interface-management#heading--manual-connections) after installation of a snap.
* Global auto-connects: some interfaces, such as `network-bind` and `audio-playback`, are automatically connected to all snaps. These interfaces are marked with ["auto-connect" in the documentation](https://snapcraft.io/docs/supported-interfaces). When a snap is installed, it will be automatically connected to any such interfaces it requests.
* Reviewed auto-connects: app developers can request additional automatic permissions for their application [using the permission request process](https://snapcraft.io/docs/permission-requests). The Snap Store team will review the security implications of automatically connecting this interface to all users of the snap.

Since the `network-bind` interface is globally auto-connected, installing this snap will immediately give it the permissions it needs.

## Building the snap

Now that all these things are in place, we can build the snap using [`snapcraft`](https://snapcraft.io/docs/snapcraft-overview). Simply open a terminal, go to this directory, and run the following command:

```shell
snapcraft --verbose
```

This will

* spin up a container or VM with the correct ubuntu version for the chosen `base`,
* download any external sources,
* install any dependencies,
* build your application,
* and package your application into a snap together with the dependencies.

The end result is the file `flaska_0.1_amd64.snap`. Congratulations, you just built your first snap! You can install it using

```shell
sudo snap install ./flaska_0.1_amd64.snap --dangerous
```

The `--dangerous` flag is to denote that this snap has not been signed, so you need to trust the source of the snap.

You can then run the command by running

```shell
flaska
```

## Turning it into a daemon

The next step is to turn the application into a service that is automatically started and restarts when it crashes. This is easy to do by changing the `app` config in `snapcraft.yaml`.

```yaml
apps:
  flaska:
    command: bin/flaska
    daemon: simple
    plugs: [network-bind]
```

The `daemon: simple` line instructs snap to run the service for as long as it is enabled. 

A snap daemon or service behaves the same as a native daemon or service, and will either start automatically at boot time and end when the machine is shutdown, or start and stop on demand through socket activation. For more information, see [services and daemons](https://snapcraft.io/docs/services-and-daemons).

After modifying the app, **rebuild the snap**, **reinstall it**, and the service should be automatically active.

* You can see all active snap services by running `snap services`.
* You can stop the service by running `snap stop flaska`.
* You can start the service by running `snap start flaska`.
* You can easily see the logs of the service by running `snap logs flaska`.

## Adding health checks

The final step is to make sure that an update won't break our application. We can do this by adding a health check _hook_ to the application. Hooks are scripts that run during actions such as installation, update and configuration of a snap. The [`check-health` hook](https://forum.snapcraft.io/t/health-checks/10605) runs immediately after installation and update, and allows you to check whether the application is working correctly.

For example, the following `check-health` script checks if the server respons to a HTTP GET to the `/health` endpoint. Add it to the snap by placing this script in the folder `snap/hooks/` as the file `check-health` (without an extension), and making it executable.

```shell
#!/bin/sh
# Wait until service comes online
sleep 2
# Try health check. If this command fails, health check fails.
curl 127.0.0.1:5000/health
```

Additionally, since this hook makes a call to the server, it needs access to the `network` interface. You can do this by adding an additional section to `snapcraft.yaml` called `hooks`:

```yaml
hooks:
  check-health:
    plugs: [network]
```

After you added this rebuild the snap, and install it. If the `check-health` hook fails after installation, the snap will immediately revert to the previous version. Try this out with a broken version of the snap. For example, modify `flaska/__main__.py` to remove the health endpoint, rebuild the snap and see the result.

There are two ways how a hook can specify that something went wrong.

1. The first way is by failing. When the `check-health` hook fails, snap reverts the snap back.
2. The second way is by using `snapctl set-health`. The advantage of this approach is that it is possible to add an additional message explaining why exactly the health check failed. For example, `snapctl set-health error "HTTP call to the webserver failed."`. For more information, see the [snapctl set-health reference](https://snapcraft.io/docs/using-snapctl#heading--health-state).

> When you're done with this tutorial, continue to [publishing a snap in the snap store](./publish-snap.md) or [trying out Ubuntu Core on a Raspberry Pi](./install-ubuntu-core.md).
