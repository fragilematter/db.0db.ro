Linux, Alsa, Skype and audio capture
####################################
:date: 2010-02-05 20:54
:author: Doru Barbu
:tags: tech, linux
:slug: linux-alsa-skype-and-audio-capture

Although I'm not a regular Skype user, I still employ it from time to
time to do my share of VoIP. But it happens quite often that I don't get
any audio from my microphone, although incoming sound works just fine
and all the alsamixer switches and gains are set properly. But, on both
of my Intel HD Audio equipped laptops this trick seems to solve the
audio capture problem just fine:

First, open a terminal and do a

.. code:: bash

  sudo alsactl store
  
Then open ``/var/lib/alsa/asound.state`` in an editor (you'll need
super-user privileges, a ``sudo nano /var/lib/alsa/asound.state`` in the
same terminal you used for the last step will do) and look for something
like:
::

            control.12 {
                    comment.access 'read write'
                    comment.type BOOLEAN
                    comment.count 2
                    iface MIXER
                    name 'Capture Switch'
                    value.0 false
                    value.1 false
            }

The numbers might differ, but the *name 'Capture Switch'* line is a
clear indicator that you've found the right control. Once you find it,
change the two *value* lines to true, so you end up with
::

                    value.0 true
                    value.1 true

Then, Ctrl-O to save your file and then Ctrl-X to exit nano (just save
the file if you're using a different editor).
Back to the console for a final command:

.. code:: bash

  sudo alsactl restore
  
Now you're free to ring up `echo123 <skype:echo123?call>`__ and test out
your new settings. Hope it helps!
