# Black Box

An application to record measurements from three sensors:

 - GPS
 - Temperature
 - Humidity
 - Air Quality

## Run

    bb.sh path/to/log/directory

## Prerequisites

- Linux system
- Python 3.7 or higher setup with VENV support
- make and wireless-tools must be installed

    sudo apt install make wireless-tools

## Setup

### Application

Once all prerequisites are installed a command can be run to setup the environment.

    make setup

### Pi Temp & Humid

    sudo apt-get install libgpiod2

### Pi GPS

Steps are from https://sparklers-the-makers.github.io/blog/robotics/use-neo-6m-module-with-raspberry-pi/

Setup Pi boot commands

    sudo vim /boot/config.txt

At the end of the file add the follwing lines:

    dtparam=spi=on
    dtoverlay=pi3-disable-bt
    core_freq=250
    enable_uart=1
    force_turbo=1

Turn off UART as a serial console

    sudo nano /boot/cmdline.txt

Delete everything and replace with

    dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles

Finally

    sudo reboot

Check data is coming from the GPS module

    sudo cat /dev/ttyAMA0

Check which service serial0 is linked too

    ls -l /dev

Command probably either

    sudo systemctl stop serial-getty@ttyAMA0.service
    sudo systemctl disable serial-getty@ttyAMA0.service

or

    sudo systemctl stop serial-getty@ttyS0.service
    sudo systemctl disable serial-getty@ttyS0.service   

## GCP setup

https://cloud.google.com/storage/docs/gsutil_install#deb

mkdir /home/volvo/blackbox
mkdir /home/volvo/blackbox/log
mkdir /home/volvo/blackbox/cold

## Testing

To test the code is up to standard

    make setup_dev
    make test