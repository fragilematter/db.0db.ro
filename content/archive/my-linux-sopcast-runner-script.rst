My Linux SopCast runner script
##############################
:date: 2010-06-01 13:33
:author: Doru Barbu
:tags: streaming, linux, script
:slug: my-linux-sopcast-runner-script

Even though I'm not a TV guy, I sometimes feel the need to watch TV. I
don't actually have a TV of my own, so I'm forced to use different kinds
of streaming frameworks. One of these frameworks is
`SopCast <http://www.sopcast.com/>`__, and although they provide Linux
binaries, the GUI isn't the most well-designed. They do have a terminal
version that makes a stream accessible on a local port, which can be
viewed in basically any player.

To make this terminal version a little more friendly, I wrote a little
script that starts up *sp-sc-auth*, leaves it a little while to buffer,
then runs vlc, directly opening the stream. When you've closed vlc,
sp-sc-auth is automagically killed too.

Here it is:

.. code:: bash

    #!/bin/sh
    sp-sc-auth sop://broker.sopcast.com:3912/6001 6555 7010 > /dev/null &
    sleep 5
    vlc http://localhost:7010/tv.asf > /dev/null &
    kill_sp_sc=`jobs -l | grep sp-sc-auth | awk '{print $2}'`
    wait_for_vlc=`jobs -l | grep vlc | awk '{print $2}'`
    wait $wait_for_vlc
    kill $kill_sp_sc

Of course, you'll need to install sp-sc-auth yourself, and you'll also
need to use the sopcast broker address for the channel of your choice. I
keep a directory full of this kind of scripts, one for each channel I
want to see. Enjoy!
