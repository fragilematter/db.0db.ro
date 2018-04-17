QtScrobble RPMs for Fedora 13
#############################
:date: 2010-07-26 15:07
:author: Doru Barbu
:tags: linux, open-source
:slug: qtscrobble-rpms-for-fedora-13

Since I have `Rockbox <http://www.rockbox.org/>`__ on a couple of my
PMPs, I like to use the log scrobbler function and when I'm near my
computer I can just submit my listened tracks history to
`Libre.fm <http://libre.fm/>`__. To do that, I use a little program
called `QtScrobble <http://qtscrob.sourceforge.net/>`__.

Unfortunately, there aren't any QtScrobble packages in the Fedora
repositories, so I decided to build one myself.

A little word of caution here: this is the first RPM package I have ever
built, so I can't know if it has any destructive capacities. All I can
vouch for is that it works on my 32-bit Fedora 13 system.

Also, I haven't really figured out if the dependencies are correctly
detected and installed. If not, you will require *Qt4*, *libcurl* and
*libmtp* to be able to run QtScrobbler.

Anyhow, to cut the story short, you can grab the RPM from here:

`http://www.mediafire.com/?0a4bawadcgzceqr <http://www.mediafire.com/file/0a4bawadcgzceqr/qtscrob-0.10-0.fm.1.i386.rpm>`__.

In case anyone else needs it, I have also uploaded the Source RPM (SRPM)
package, get it here:

`http://www.mediafire.com/?g4gll2tfomx88t6 <http://www.mediafire.com/file/g4gll2tfomx88t6/qtscrob-0.10-0.fm.1.src.rpm>`__

Any feed-back will be greatly appreciated. Enjoy!

Note: I've also tested the package on OpenSUSE 11.3 and it works. YMMV
:)
