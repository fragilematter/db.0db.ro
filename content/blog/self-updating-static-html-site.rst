Content?
##########################################
:date: 2019-02-27 21:13
:author: Doru Barbu
:tags: blog tech
:slug: self-updating-static-html-site

I like static html, it's secure, uses few resources and, theoretically, loads 
quickly. It only sucks when you want to update the content.

Static site generators help with the updating part, but you're not going to 
have a full python stack, pelican and your sources everywhere you go. But if 
you have the space and resources on your VPS to run your static site generator, 
maybe during the off-peak hours, it's very easy to have an auto-updating static 
site.

The sources can live happily on 
`Github <https://github.com/fragilematter/db.0db.ro>`_ and you can use the 
built-in web editors to add or update content at your whim. The other part of 
this self-updating combo is a cron script that pulls the git repo, runs pelican 
and, as long as everything went well, copies the output files to your www root.

That's what this tiny script does, I have it scheduled to run every night:

.. code-block:: bash

  #!/bin/sh
  cd ~/0db_pelican/
  git pull origin master
  if [ "$?" -ne "0" ]; then
    echo "git failed"
    exit 1
  fi
  pelican -o output -s pelicanconf.py content
  if [ "$?" -ne "0" ]; then
    echo "pelican failed"
    exit 1
  fi
  cp -r ~/0db_pelican/output/* ~/www/

