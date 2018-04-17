Enable mp3 ringtones on Motorola W490/W510
##########################################
:date: 2010-02-05 20:53
:author: Doru Barbu
:tags: tech, mobile
:slug: enable-mp3-ringtones-on-motorola-w490w510

Just in case you have one of those pesky Motorola W490 or W510 mobile
phones that can't use an mp3 file as a ringtone because your network
provider doesn't want to let you do that, well, you can. And you won't
have to reflash your phone just to do that, a simple seem edit is enough
to do the trick. I won't go over the whole theory of seem editing, if
you're not familiar with that, there are plenty of forums and websites
on which the process is explained.

The seem in question is 0032_0001, at offset 0xC7 you will find a 0x00
value (or at least that was the value in the particular firmware version
that my phone had). All you have to do is a little bit manipulation and
enable bit 2. The new value is 0X04, and it did the trick for me. If
you're using XVI32 to edit the file, it should go like this:

|XVI32 editing seem 0032_0001|

I couldn't find this particular seem modification documented anywhere,
so I hope it might be useful for someone. Happy modding!

**Later Edit:** The initial values might differ, but I have confirmed
that bit 2 needs to be enabled for MP3's to be applied as ringtones.

.. |XVI32 editing seem 0032_0001| image:: |filename|/images/archive/W490-mp3-ringtones_small_001.png
   :target: |filename|/images/archive/W490-mp3-ringtones_large_001.jpg
