Mp3 To Mp4plus script update
############################
:date: 2010-02-05 20:54
:author: Doru Barbu
:tags: muzica, telefonie mobila, linux, open-source
:slug: mp3-to-mp4plus-script-update

This is just an update to the script I posted a while ago `over
here <http://fragilematter.blogspot.com/2009/03/quick-audio-conversion-script.html>`__.
It works the same, has the same requirements, it's just a bit more user
friendly.
Refer to `the original
post <http://fragilematter.blogspot.com/2009/03/quick-audio-conversion-script.html>`__
for details, grab the script below.

.. code:: bash

  #!/bin/sh
  if [ $# -lt 3 ]then
    echo Usage: $0 \<infile\> \<outfile\> \<bitrate\>
  else    
    mplayer -quiet -vo null -vc null -ao pcm:waveheader:file="/tmp/$$.wav" -af resample=48000:0:1 "$1"    
    normalize-audio --peak "/tmp/$$.wav"    
    aacplusenc "/tmp/$$.wav" /tmp/$$.aac "$3"    
    MP4Box -new -no-sys -sbrx -add /tmp/$$.aac "$2"    
    rm -f /tmp/$$.aac /tmp/$$.wav
  fi
