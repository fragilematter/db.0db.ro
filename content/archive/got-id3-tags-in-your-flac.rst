Got id3 tags in your flac?
##########################
:date: 2012-05-28 18:03
:author: Doru Barbu
:tags: tech
:slug: got-id3-tags-in-your-flac

Id3 tags are busting your flac party (especially with
`acxi <http://techpatterns.com/forums/about1491.html>`__/oggenc choking
with ``ERROR: Input file [...] is not a supported format``)? Just grab
yourself a copy of `id3v2 <http://id3v2.sourceforge.net/>`__ and run it
like

.. code:: bash

  id3v2 -D ./*.flac

If you're rocking the party with Arch Linux, you can find both id3v2 and
acxi in the `AUR <http://aur.archlinux.org/>`__.

There, that fixed it.
