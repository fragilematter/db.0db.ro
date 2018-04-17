ASUS WL-AM604G NARS-enabled firmware
####################################
:date: 2010-02-05 20:52
:author: Doru Barbu
:tags: tech, net, linux, open-source
:slug: asus-wl-am604g-nars-enabled-firmware

If you have an ASUS WL-AM604G (A hardware variant) ADSL Wireless router,
than you are probably accustomed to rebooting it everytime your
connection fails and your ISP returns an invalid username/password
error.
Fortunately, the sources for this router's Linux-based firmware are
available, and a group of russian modders have made some serious
modifications to a similar type of router produced by ASUS - the AM604,
including a fix for this reconnect problem.
They called it the NARS reconnect patch and, since the two devices are
extremely similar, getting it to work on the WL-AM604G posed no problems
at all. This modified firmware had been running for more than a month on
my router without any problems whatsoever, so I decided to make it
available to anyone who wishes to use it. I have yet to clean up and
release the modified source files, but I will do so upon request.

WARNING: The firmware update process isn't risk free. Although this
firmware had been verified and it is known to work on my router, it is
made available without any warranty. You are solely responsible to using
it and any problems that might arise from that. Also, this firmware is
ONLY compatilble with the A hardware variant.


If you haven't been frightened by the warning above, download the file
linked below and open your router's `administration
panel <http://192.168.1.1/>`__. Go to the firmware update page and click
the *Choose* button, then select the file you previously downloaded. The
firmware update takes a couple of minutes, and there won't be any
visible modifications or improvements to the way the administration
panel looks and works. ***It is advisable that the firmware update
operation is carried out through an ethernet cable, since the wireless
connection is less reliable.*
**Bad flash recovery**
If you are certain that your router has ceased to function, follow these
steps to recover it:
**

#. Go to the
   `ASUS <http://support.asus.com.tw/download/download.aspx?product=11&model=WL-AM604g&SLanguage=en-us&os=8>`__
   support page and download an official firmware.
#. Turn off the router.
#. Push the reset button on the router with a thin object and hold it
   pressed wile you power on the router.
#. The *Power* LED should start to blink slowly. If it doesn't, resume
   from step 2.
#. Connect the computer to the router through an ethernet cable, and
   give it a 192.168.1.x IP, with 2<x<255, netmask 255.255.255.0.
#. Open a Command Prompt/CMD/terminal and change directory to where you
   downloaded the firmware. Run
   ``tftp -m binary 192.168.1.1 -c put nume_firmware.trx``. There is no
   progress indication, so wait a couple of minutes for the operation to
   complete.
#. Stop and re-start the router, everything should be ok. If it doesn't,
   resume from step 2.

| **Download:** http://www.mediafire.com/?y1am0jvwjkn
| **SHA1:** 67f27458b97f711abcda928e15f7f385451435cf
| **MD5:** 534f60677a5efe02817d2cb937d77a56
| **CRC32:** 686797e6
