A Better GNU chroot for Android Phones Using Raspbian
#####################################################
:date: 2013-02-17 17:58
:author: Doru Barbu
:tags: chroot debian raspbian ARMv4
:slug: a-better-gnu-chroot-for-android-phones-using-raspbian

A common way to get all of the GNU/Linux utilities on an Android phone
is to set up a chroot environment, either on a dedicated partition or in
a filesystem image. Both methods yeld the expected results, but the
source of those files can make a difference. For instance, Debian armel
binaries are `compiled for ARMv4 and
higher <http://wiki.debian.org/ArmEabiPort>`__ architectures with no
support for hardware floating point functionality, while the newer armhf
EABI targets `ARMv7 and
newer <http://wiki.debian.org/ArmHardFloatPort>`__ processors. This
means that ARMv5 and v6 processors with the `vector floating
point <http://en.wikipedia.org/wiki/ARM_architecture#Floating-point_.28VFP.29>`__
unit get no love. However, with the introduction of the Raspberry Pi,
which sports an ARMv6 processor, demanding mobile phone users can steal
a bit of the love.

I've done this on a MSM7227-powered LG Optimus One (P500), but the same
cpu can be found in a lot of phones, like the older Galaxy Mini, the
Optimus Me and `the list could
continue <http://phonedb.net/index.php?m=processor&id=310&c=qualcomm_msm7227a__snapdragon_s1>`__.
However, this should work on other, possibly newer processors too.
Enough of the chatter, let's see how we can get a Raspbian chroot on the
phone.

.. code:: bash

  dd if=/dev/zero of=raspbian.img bs=1 count=0 seek=1G
  mkfs.ext2 raspbian.img
  tune2fs -c0 raspbian.img
  mount -o loop,rw raspbian.img /mnt
  debootstrap --foreign --no-check-gpg --include=ca-certificates --arch=armhf wheezy /mnt http://archive.raspbian.org/raspbian
  umount /mnt/
  debootstrap --second-stage
