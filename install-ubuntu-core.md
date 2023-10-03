# Install Ubuntu Core on a raspberry pi and test it out

If the demo-gods bless us and the conference venue permits, you can try out Ubuntu Core on our supplied raspberry pi's.

## Ensure your Ubuntu One account has an SSH key attached

1. Go to [Launchpad](https://launchpad.net/) and login with your Ubuntu One account.
1. Click on your profile and click the edit button next to `SSH Keys`. You can add your own SSH key there, or use the one already provided in the VM.
   * To show the public key of your ssh keypair, run `cat ~/.ssh/id_rsa.pub`. Copy this text and paste it as a new key in launchpad.

## Installation and initial setup

Follow the tutorial [Install Ubuntu Core on a Raspberry Pi](https://ubuntu.com/download/raspberry-pi-core).

> Note that you can run the Raspberry Pi imager on any OS. It might be easier to install it on your laptop instead of in the VM.

> When moving Ubuntu Core into production, you will want to create your own Ubuntu Core image, with your own snaps and configuration pre-loaded. To get started, see [Build your own Ubuntu Core image](https://ubuntu.com/core/docs/build-an-image). With this approach, you will not need to login when the device first boots. Instead, the device is ready to go immediately after you flash the image!

## Install snaps

> Note: you can test this out both on your computer and on the raspberry pi.

Many snaps in the [Snap Store](https://snapcraft.io/store) work on Ubuntu Core on a raspberry pi. There are three limitations:

* The snap should support the raspberry pi architecture (ARM64)
* The snap should be using `strict` confinement. Snaps with `classic` confinement only work on traditional Linux systems.
* Most GUI applications will not work by default on Ubuntu Core without modification (more on that further on this page).

## Install Docker containers

> Note: you can test this out both on your computer and on the raspberry pi.

Working with Docker containers on Ubuntu core almost exactly the same as working with docker on traditional Ubuntu. For example, run the following command to install Docker and run a hello-world container.

```shell
sudo snap install docker
sudo docker run hello-world
```

## Try a GUI application

> Note: you can test this out both on your computer and on the raspberry pi.

The first step is to install GUI app support:

```shell
sudo snap install ubuntu-frame --channel=22
```

After that, you can install any "Ubuntu Frame"-compatible app. For example, the following app allows you to open a webpage in kiosk mode.

```shell
sudo snap install wpe-webkit-mir-kiosk
```

You can also configure the kiosk to point to a local webserver instead.

```shell
sudo snap set wpe-webkit-mir-kiosk url=http://localhost:5000
```

For more information about this web kiosk, take a look at [the wpe-webkit-mir-kiosk README](https://gitlab.com/glancr/wpe-webkit-snap/-/blob/main/README.md).

For a thorough introduction to Ubuntu Frame and GUI applications on Ubuntu Core, see the [Guide for embedding IoT GUI with Ubuntu Frame](https://discourse.ubuntu.com/t/guide-for-embedding-iot-gui-with-ubuntu-frame/29079) or [Read the whitepaper](https://pages.ubuntu.com/rs/066-EOV-335/images/Guide_for_embedding_IoT_GUI_with_Ubuntu_Frame_31_03_23.pdf).

## Try MicroK8s

> Note: you can test this out both on your computer and on the raspberry pi.

* To get started with MicroK8s on Ubuntu Core, follow the tutorial [Getting started with MicroK8s on Ubuntu Core](https://ubuntu.com/tutorials/getting-started-with-microk8s-on-ubuntu-core#1-introduction)
* To get started with MicroK8s on traditional Ubuntu, follow [the getting started docs](https://microk8s.io/docs/getting-started)
