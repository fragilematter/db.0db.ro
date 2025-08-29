Flash Drive Web Browser Stress Test
###################################
:date: 2010-02-05 20:57
:author: Doru Barbu
:tags: tech
:slug: flash-drive-web-browser-stress-test

Recently I had some unvoluntary *fun* concerning one of my flash drives.
After that I decided to encrypt a part of my Portable Apps Suite that I
keep on it, mainly the web browser, Pidgin, PuTTy and WinSCP, the
sensitive stuff.

Playing with TrueCrypt I observed that it is able to show how much was
read/written from the encripted drive in a session - a potential tool to
see how much can a web browser stress a flash drive.

So I devised a simple set of tests to compare `Portable
Firefox <http://portableapps.com/apps/internet/firefox_portable>`__ and
`Opera@USB <http://www.opera-usb.com/operausben.htm>`__.

I optimised the browsers as much as possible for flash drive operation
(no disk cache, limited back/forward entries).

The first test was just to plug in the drive, let
`geek.menu <http://geek-menu.sourceforge.net/>`__ mount the encrypted
container, fire up the browser from the menu, wait 'till the drive led
stops blinking, close the driver, wait again. These were the results:

|Flash Drive Browser start - Opera|
|Flash Drive Browser start - Firefox|

| (Top - Opera, Bottom - Firefox)

As you can see, Firefox read about four times more data than Opera and
wrote about 18 times more. Clearly, Opera's executable is well packed
and optimised.

Then I browsed using both Firefox and Opera through a series of websites
I picked, trying to have some diversity. So, these are the sites:

.. code:: html

  http://www.youtube.com/watch?v=hVeEMrXGMww
  http://acid3.acidtests.org/
  http://blogdeaberat.wordpress.com/
  http://www.scribd.com/doc/11537792/ubuntu-pocket-guide-v11
  http://ubuntu.ro/
  http://friendfeed.com/public?format=atom
  http://gpl.internetconnection.net/vi/

No surprises here:

|Flash Drive Browser test - Opera|
|Flash Drive Browser test - Firefox|

| (Top - Opera, Bottom - Firefox)

As you can see, Opera barely scratched the drive, it just loaded itself
and saved cookies probably. Firefox on the other side got about 40 megs
of data, and put back nearly as much.

Now, if you count in that Opera also has a (limited) torrent client,
feed reader, e-mail client, irc client, built-in sync capability and
also the widget engine that I never use, it is a great tool to carry
around.

Firefox is the memory hog that we all know and the xulrunner framework
that allows you to run the myriad of add-ins is great for a desktop
computer, but the performance penalty is quite big to make a for a
enjoyable portable experience.

.. |Flash Drive Browser start - Opera| image:: {static}/images/archive/JustStart_Opera.png
   :target: {static}/images/archive/JustStart_Opera.png
.. |Flash Drive Browser start - Firefox| image:: {static}/images/archive/JustStart_Firefox.png
   :target: {static}/images/archive/JustStart_Firefox.png
.. |Flash Drive Browser test - Opera| image:: {static}/images/archive/FullTest_Opera.png
   :target: {static}/images/archive/FullTest_Opera.png
.. |Flash Drive Browser test - Firefox| image:: {static}/images/archive/FullTest_Firefox.png
   :target: {static}/images/archive/FullTest_Firefox.png
