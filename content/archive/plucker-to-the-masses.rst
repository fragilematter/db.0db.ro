Plucker to the masses
#####################
:date: 2008-12-26 08:35
:author: Doru Barbu
:tags: linux, open-source
:slug: plucker-to-the-masses

Here's a little shell script I made to convert the html files in a
directory to plucker format e-books:

.. code-block:: bash

  #!/bin/sh
  ORIGINAL_IFS=$IFS
  IFS=$'\n'
  for file in $1*.html; do 
    plucker-build -f $2`basename $(echo $file|sed -e "s/ /\\\ /g") .html` file:$file
  done
  IFS=$ORIGINAL_IFS`

You call it like ``./pluckerbatch.sh /source/dir/ /dest/dir/`` - take care
when writing the dir paths not to omit the trailing slashes as I did not
compensate for them, the scripts expects them to be there.

As you can see, it's a very hackish approach made just to speed up a
particular job, so it expects that the source dir only has html files
(anything in that folder is sent to plucker-build) and it may have some
problems. It should be safe when it encounters paths with spaces
though...

I hope it'll be useful to someone else!
