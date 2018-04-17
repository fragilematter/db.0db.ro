Installing Tiny Core Linux on a USB drive
#########################################
:date: 2010-09-18 12:40
:author: Doru Barbu
:tags: virtual matters, linux, open-source
:slug: installing-tiny-core-linux-on-a-usb-drive

There's a lot of reasons to have a portable USB Linux setup that does
something else than actually duplicating the Live CD of distro X. With
Tiny Core that's different, since it does away with the solid squashfs
setup that most live distros have and, if you follow the steps outlined
in this tutorial, you'll also get a real home folder, not some
copy-on-write persistence loopback file.
Note: the following tutorial has been originally written as a plain text
file and it is presented below as such.
Some commands, if not run carefully, can become dangerous to your data,
so I can only advise you to keep your eyes open for any mistakes. Other
than that, I'm open to questions, so don't hesitate to leave a comment.

| 

::

                    == Installing Tiny Core on a USB drive ==
                               == the ext2 way ==


      In this tutorial I will walk you through installing Tiny Core Linux on a
    USB drive in a way that will enable it to maintain top speed while including
    useful features like persistence and low RAM usage.

    * Prerequisites:
      - an existing Linux system with fdisk and extlinux;
      - an USB drive >= 128MB;


    * Getting the goods.
      Since we're talking Tiny Core here, we might as well start with getting the
    ISO image that will form the base of our fresh USB drive installation. The
    latest version can always be found at:

    http://distro.ibiblio.org/pub/linux/distributions/tinycorelinux/3.x/release/tinycore-current.iso

      Just get it with wget or something, it's a small download.
    With that taken care of, it's time to prepare the USB drive.

    * Preparing the USB drive.
      I'm assuming that the USB drive you'll be installing to is a spare one that
    you have laying around. If that's not the case, back up everything from it,
    since the next step _WILL WIPE IT CLEAN_.
      Also, all the following utilities require super-user permissions, so you will
    either have to prefix their respective commands with "sudo", or just go with
    "su" once.
      With the drive firmly inserted into a USB port, you'll want to umount it.
    Then open a terminal and, replacing X with the appropriate letter, do a:

    fdisk /dev/sdX

      Fdisk will open and will present you with an interactive mode that requires
    you to enter one letter commands. I will further write these commands in this
    form: [C], meaning that you'll press the "c" key then Enter.

      First up, we will disable DOS compatibility, since it's of no use to us or
    to Tiny Core. Enter [C], and fdisk should reply with "DOS Compatibility flag
    is not set." Then press [U], so that everything will be displayed in sectors
    instead of cylinders {EW!}.

      With that out of the way, we want to make sure that the partition table on
    the USB drive is in order, and we'll do that with [O]. That should return
    "Building a new DOS disklabel with disk identifier {some hex value}."

      Now that we're all set up, it's time to create the ext2 partition that will
    receive our fresh Tiny Core setup. To do that, enter [N], then [P], then [1].
    For the first sector and last sector inputs, just confirm the default values
    by pressing Enter. This whole series of commands created for us a primary
    partition that covers the whole drive.

      A couple more commands, and we'll be done with fdisk. We'll want to set the
    partition type to 83, to mark it as a Linux partition. That can be achieved
    with [T] followed by [83]. Then we'll mark the partition as active by pressing
    [A], then [1]. This way the systems that will be booting from the USB drive
    will know on what partition to look for the files - partition 1 in our case.

      That pretty much concludes the fdisk step, so we'll write everything to disk
    by pressing [W]. Fdisk should say "The partition table has been altered!", then
    quit.

      Now we have a USB drive with a neat partition, but we have no filesystem.
    Time to create one:

    mkfs.ext2 -L "tc" /dev/sdX1

      Of course, replace X with the appropriate letter for the USB drive. The
    mkfs.ext2 command just created an ext2 filesystem on the partition, and labeled
    it "tc".

      Now the most comfortable step to have the partition mounted and to make sure
    that the kernel is up to date with the modifications we made is to run

    eject sdX

    then pop the USB out of the port and insert it back. By now your desktop
    environment should have automagically mounted the partition to /media/tc.
    I will assume that is the case, so all the following commands will reflect
    that situation. If it's different in your case, alter them accordingly.

    * Getting TinyCore on the USB drive
      Now that we have a clean base for our install, it's time to proceed. To place
    the required files on there, we'll first need to access them, by mounting the
    ISO image. Easy, right?

    mount -o loop -t iso9660 tinycore-current.iso /mnt

      This made the contents of the ISO image accessible in the /mnt folder. Now
    to copy them onto the USB partition:

    cp -R /mnt/boot /media/tc/

      We're done with the ISO image, so we might as well get rid of it.

    umount tinycore-current.iso
    rm tinycore-current.iso

      We have the files on the USB drive, but they came from a CD, so the
    bootloader configuration is tailored for CD media. Let's fix it:

    cd /media/tc/boot/
    mv isolinux extlinux
    mv extlinux/isolinux.cfg extlinux/extlinux.conf
    rm extlinux/isolinux.bin

      You may have noticed "extlinux" pop up in those commands. That is the
    bootloader we're gonna use. We could have used grub, but I don't think the
    added complexity is really warranted in our simple boot case. We won't be
    taking care of the bootloader install right now, we'll leave that for last.

      We also need to make a couple of directories that Tiny Core needs:

    mkdir -p /media/tc/tce/optional
    mkdir /media/tc/opt

      What we will take care of is tuning the boot parameters so that Tiny Core
    will know what devices to use and how to use them for maximum performance.
      As you'd expect, the drive designation won't stay the same as the USB drive
    is used on different computers, so we need another way of referring to it
    instead of /dev/sdX1. Luckily, when we formatted the partition, it also
    received a unique identification in the form of a long alphanumeric string.
      To find out that string, we need to run:

    blkid -s UUID /dev/sdX1

      This command will output something along the lines of
    /dev/sdX1: UUID="{some long string}" - copy the UUID= part, because we
    will need it in this next step.

      Now open extlinux/extlinux.conf in your favorite text editor. This file
    contains several lines that detail what kernel to use and how that kernel
    should be started. We are interested in the "append initrd={...} line.
    To this line we are going to add several things:

    waitusb=5 tce=UUID="..." restore=UUID="..." home=UUID="..." opt=UUID="..."

      Note that you will need to insert the actual UUID string that you obtained
    from the blkid command instead of "...". Also, the file might be read only, but
    that can be quickly fixed with a "chmod +w extlinux.conf"
      Let's go over the added tags:
      - waitusb=5 tells tiny core to wait for 5 seconds before searching for USB
    devices. This might be needed in case the drive isn't detected that fast.
    You're free to try smaller values, or remove the waitusb bit completely.
     However, I advise you to keep it for compatibility reasons.
      The other four parameters (tce, restore, home, opt) tell Tiny Core to store
    packages on the USB drive, to look for back-ups in there and, finally, to place
    the home and opt folders on that same partition.
      Additionally, you might want to add some other parameters. You can read all
    about those in the extlinux folder, by opening the text files named "f2"
    and "f3".

      We're almost done, it's time to add that missing bootloader. Assuming that
    you have syslinux/extlinux installed, it's just a matter of running

    extlinux -i /media/tc/boot/extlinux

      This doesn't output much, but it does give us an info that we'll use in the
    next step: "/media/tc/boot/extlinux is device /dev/sdX1". Remember that 
    "/dev/sdX" part.
      With that we've taken care of the partition boot sector, but that doesn't
    mean that the USB drive's master boot record is as we want it to be. Again,
    assuming that you have syslinux installed, you can fix that quickly:

    cat /usr/share/syslinux/mbr.bin > /dev/sdX

    where "/dev/sdX" is the device that was identified by extlinux. Also note that
    the trailing "1" was omitted, since we are referring to the whole USB drive,
    not the first partition.

      That's it, we're mostly done. The Tiny Core install is ready, all you need
    to do now is make sure all the data has been written to disk, then you can
    reboot and take it for a spin:

    cd /
    eject sdX
    reboot

    * Finishing notes
        Once you have booted your fresh new TinyCore install, you should edit the
    /opt/.filetool.list text file, and remove the "home/" line. That way, you
    won't end up with large quantities ofduplicate copies of  files on the
    partition and in the back-up when you shutdown the system.
      This tutorial covers only a small portion of what you can do with Tiny Core.
    If you want to do more complex things, read up on what can be achieved with
    this operating sistem at http://tinycorelinux.com/. Also, the wiki has quite
    a lot of valuable information - http://wiki.tinycorelinux.com/tiki-index.php
