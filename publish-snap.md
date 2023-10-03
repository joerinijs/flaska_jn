# Publishing your first IoT snap

As you might have noticed, the snap you built in the previous tutorial is built for the `amd64` CPU architecture. However, many IoT devices use an ARM processor. The Snap Store has a free and open source build service that lets you compile your snap for a number of different architectures, including `arm64` and `armhv`.

To use this build service, take the following steps.

## Put the source code of your snap on GitHub

1. Rename your snap to a unique name, in order to avoid conflicts with other participants of this workshop. For example, you can suffix `flaska` with your own name.
1. Upload your snap source repository (this repository) to GitHub.

## Register the name of your snap in the Snap Store

1. Create an [Ubuntu One](https://login.ubuntu.com/) account. For more detailed info, see [Create a developer account](https://snapcraft.io/docs/creating-your-developer-account)
1. Surf to the [Snap Store](https://snapcraft.io/), log in with your Ubuntu One account, and click `register a snap name`. For more detailed info, see [Registering your app name](https://snapcraft.io/docs/registering-your-app-name)

## Setup the build service

In the snap store dashboard, click on the name you just registered, and select the `Builds` tab. There you can connect the GitHub repository you just created to the build service.

By default, the build service will build your snap for all available architectures.

> Note: you do not _need_ to use the build service. You can also [upload the snap you just built locally using the CLI](https://snapcraft.io/docs/releasing-your-app).

## Releasing the snap

After a build has finished successfully, you can release a certain revision of your snap in the `Releases` tab of your snap's store dashboard.

After you release your snap, it is now available to install on any device supporting snap, simply by running `snap install SNAPNAME`.

> When you've published your first snap, [install Ubuntu Core](./install-ubuntu-core.md) on a raspberry pi to download and run it.
