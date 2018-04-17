Minimal Rockbox scrobbler.log to libre.fm submitter
###################################################
:date: 2010-08-30 19:56
:author: Doru Barbu
:tags: linux, script, open-source
:slug: minimal-rockbox-scrobblerlog-to-librefm-submitter

I've recently found myself on a severely resource-limited computer, and
I tried to find a way to submit my listening history from my
`Rockbox <http://www.rockbox.org/>`__ device to
`libre.fm <http://libre.fm/>`__ without needing a lot of dependencies.
After a bit of searching I stumbled upon a script made by a couple of
Linux Outlaws listeners, back on the `LO
forum <http://linuxoutlaws.com/forums/viewtopic.php?f=10&t=1592&p=26163>`__...
but it had a couple of glitches.

The script only works as a converter from the scrobbler.log format to
the one used by import.py - a libre.fm migration tool, so you
basically needed to run a couple of commands just to upload some
tracks.

Another hassle was that the script didn't filter the skipped tracks,
effectively spamming my listening history with songs I didn't feel
like listening that day. Also, the duplicate entries weren't filtered
either.

I've modified the script to fix those issues, and to invoke import.py
automagically for you.

Just save it as somename.sh in a folder of your choice, along with
`import.py <http://svn.savannah.gnu.org/viewvc/*checkout*/trunk/lastscrape/import.py?root=librefm>`__
and
`gobble.py <http://svn.savannah.gnu.org/viewvc/*checkout*/trunk/scripts/gobble.py?root=librefm>`__
from the libre.fm project. Then edit it and change line 46 with your
username.

If you don't need automatic scrobbling, comment lines 46 and 47, and a
rockbox.log file with be left in the current folder, for you to
manually import.
Run it with ./somename.sh /path/to/your/rockbox/player/mount/point

Here's the script:

--------------

::

    #!/bin/bash
    #A script to convert Rockbox .scrobbler.logs to a format suitable for libre.fm
    #Just run this script as "./scrobble.sh /path/to/scrobbler_log_file"
    #You may have to change the timezone (on line 20 I.E. UTC+1 = British summer time)
    # to suit your timezone if you get errors.
    #The file can then be uploaded via the import.py script found here
    # http://ideas.libre.fm/index.php/Using_lastscrape
    #Place import.py and gobble.py in the same folder as the script for automatic
    # submission, otherwise comment lines 46 and 47 (by adding a "#" in front).

    #Remove the uneeded info

    cat $1/.scrobbler.log | grep -Pv "\tS\t" | sed '1,3d' | cut -f 1,3 > /tmp/scrobtracks.tmp


    #convert timestamps from epoch time to human readable

    cat $1/.scrobbler.log | grep -Pv "\tS\t" | sed '1,3d' | cut -f 7 | while read line
    do
    date -d '1970-01-01 UTC+3 '$line' seconds' +"%FT%TZ" >> /tmp/scrobdate.tmp
    done


    #build finished file

    paste /tmp/scrobtracks.tmp /tmp/scrobdate.tmp > /tmp/scroblog.tmp

    awk '!x[$0]++' /tmp/scroblog.tmp > ./rockbox.log

    NUM=`cat /tmp/scrobdate.tmp | wc -l`

    clear
    echo "-------------------------------------------"
    echo ": There are $NUM tracks in your rockbox.log :"
    echo "-------------------------------------------"

    rm /tmp/scrobdate.tmp
    rm /tmp/scrobtracks.tmp
    rm /tmp/scroblog.tmp

    echo ""
    echo ""
    echo "Finished processing"
    echo "Starting import"
    echo ""
    ./import.py -s http://turtle.libre.fm/ YOUR_LIBRE.FM_USERNAME ./rockbox.log
    rm ./rockbox.log
    rm $1/.scrobbler.log
    echo ""
    echo ""
    echo "Done"
    echo ""

--------------

EOF
 