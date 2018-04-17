Quick audio conversion script
#############################
:date: 2010-02-05 20:56
:author: Doru Barbu
:tags: soft power, telefonie mobila, linux, open-source
:slug: quick-audio-conversion-script

Wow, I haven't been here in a while.
Anyhow, since I'm playing quite alot with mobile phones, I needed a way
to convert my podcasts to a less space consuming format. And since all
of them support HE-AAC, I wrote a small wrapper script that can convert
almost any format accepted by mplayer to m4a (aac audio in am mp4
container). Grab it below!

.. code:: bash

  #!/bin/sh
  mplayer -quiet -vo null -vc null -ao pcm:waveheader:file="/tmp/$$.wav" -af resample=48000:0:1 "$1"
  normalize-audio --peak "/tmp/$$.wav"
  aacplusenc "/tmp/$$.wav" /tmp/$$.aac "$3"
  MP4Box -new -no-sys -sbrx -add /tmp/$$.aac "$2"
  rm -f /tmp/$$.aac /tmp/$$.wav``

In Ubuntu you will need to get the following packages:

-  mplayer (of course)
-  aacplusenc from `medibuntu <http://www.medibuntu.org/>`__
-  normalize-audio
-  gpac (for MP4Box)

Also, as you can see, I had mplayer convert the audio to a 48kHz
sampling rate - that's because aacplusenc would convert the audio to
that sampling rate anyways, and I trust mplayer's conversions to be more
accurate.

I could probably use pipes between the programs so less temporary data
is written to disk, but it works pretty fast this way and I'm pretty
lazy...

Let's get to **usage**: just copy the stuff above to a file, let's say
*tomp4.sh*, then open a terminal and do a ``chmod +x ./tomp4.sh``. To use
it simply call it from a terminal like this: ``./tomp4.sh infile.mp3
outfile.m4a bitrate``. I mostly use a bitrate of 24 kbps for podcasts and
48kbps for music.

Enjoy!
