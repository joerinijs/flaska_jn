# Ubuntu Core Workshop

Welcome to the Ubuntu Core workshop! For an introduction, take a look at [the introductory presentation](https://docs.google.com/presentation/d/1QfimuD6Np7FYDX1C1LtbVfTfoo836iiBROZ7NiyHhDs/edit?usp=sharing).

## Getting started

Download the virtual machine for your hypervisor of choice:

* VirtualBox: https://cloud.ilabt.imec.be/index.php/s/4AYaQSJeYDEdYxL
* VMWare: https://cloud.ilabt.imec.be/index.php/s/BS4n37bsJTsGERi

Run the VM and check if you have network connectivity. If you do, run the following commands in a termninal.

```bash
git clone https://github.com/idlab-discover/flaska.git
code flaska
```

This will open Visual Studio Code in the project assigment repository. Now you're ready to get started!

## Contents

* [Build your first IoT snap](./first-snap.md)
* [Publish your first snap to the Snap Store](./publish-snap.md)
* [Install Ubuntu Core, run snaps, Docker containers, and GUI apps](./install-ubuntu-core.md)

## Extra

When moving Ubuntu Core into production, you will want to create your own Ubuntu Core image, with your own snaps and configuration pre-loaded. To get started, see [Build your own Ubuntu Core image](https://ubuntu.com/core/docs/build-an-image).

## Copyright

* The code in this repository is licensed MIT
* The documentation in this repository is licensed CC-BY

Feel free to reuse, and remix it, but [let me know](mailto:merlijn.sebrechts@ugent.be) if this is useful to you!.
