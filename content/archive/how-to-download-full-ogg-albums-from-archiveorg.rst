How to download full ogg albums from archive.org
################################################
:date: 2010-09-20 20:30
:author: Doru Barbu
:tags: virtual matters, net, open-source
:slug: how-to-download-full-ogg-albums-from-archiveorg

If you download files from `archive.org <http://www.archive.org/>`__'s
audio section, you probably observed by now that, while there are
options to download all the files in 64Kbps or variable bitrate MP3,
there is no ogg download of the same type.

Don't forge ahead right clicking all individual ogg downloads, we can
get some open source software to help.

For example purposes, let's pick some `Blind Willie
McTell <http://www.archive.org/details/BlindWillieMctell>`__ music.
There are only three songs there, but it should be enough for you to get
the basic idea.

The first step is quite simple: we need to get a list of links towards
those ogg files. If you're using Firefox, all you need to do is to
expand the list of songs on the left side of the page, under the MP3 zip
downloads, then select all its text, right click it and choose "View
Selection Source". It's a bit complicated to explain, but this
screenshot should help:

|image0|

If you aren't using Firefox, just open the source of the page (CTRL+U in
most browsers) and search for the first instance of the string ".ogg".
It should occur around line 222, and nicely included in some divs will
be that list of links that I was referring to.

Just copy that bit of html and pop it into a text editor of your choice,
then save it, call the file "links.html" for example.
And now for the real action, let's call upon that open source help. It's
something along the lines of:

.. code:: bash

  wget -Fi links.html -B http://www.archive.org

What we're doing here is asking wget to download all the files referred
to in links.html. The catch is that the links are relative to the server
root so, with the aid of the "-B" parameter, we're basically telling
wget that the server is archive.org.

That's all, hope it helps someone!

.. |image0| image:: {static}/images/archive/page_source_ogg_links.png
   :target: {static}/images/archive/page_source_ogg_links.png
