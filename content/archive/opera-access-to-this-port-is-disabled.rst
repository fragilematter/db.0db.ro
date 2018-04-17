Opera - Access to this port is disabled
#######################################
:date: 2011-02-20 14:13
:author: Doru Barbu
:tags: virtual matters, net
:slug: opera-access-to-this-port-is-disabled

You're happily browsing the interwebs in Opera, and you suddenly get a
big red error: Access to this port is disabled for security reasons.,
just like in the image below. Who you gonna call? Read on...

|image0|

We just need to pop Opera's hood open and do a little tuning. So open a
new tab and go to this address: opera:config

I can't remember for sure, but it might give you a warning that you
might break stuff... just plow ahead. Eventually that bold red title
should read Preferences editor. Underneath that title is a search box,
and we're gonna use it to scour the preferences for the word ports.
It should look like this:

|image1|

Once you found it, pop the port number into the text box that says
Permitted Ports. The port number is the bit just after the website's
main address, delimited by a colon on the left and a slash on the right.

So, for ``http://gopher.info-underground.net:70/``, the port number is,
of course, ``70``. If you want to allow access to more than one port,
separate them with semicolons. Now click save, press the OK button of
the messagebox that appears, close the tab then refresh your page.

Voila:

|image2|

.. |image0| image:: |filename|/images/archive/op_port_1.png
   :width: 400px
   :height: 185px
   :target: |filename|/images/archive/op_port_1.png
.. |image1| image:: |filename|/images/archive/op_port_2.png
   :width: 400px
   :height: 215px
   :target: |filename|/images/archive/op_port_2.png
.. |image2| image:: |filename|/images/archive/op_port_3.png
   :width: 400px
   :height: 179px
   :target: |filename|/images/archive/op_port_3.png
