Squashfs Tools 4.0 Windows Binaries
###################################
:date: 2015-05-14 06:11
:author: Doru Barbu
:tags: linux, open-source
:slug: squashfs-tools-40-windows-binaries

**DomoticX** has built a set of varying versions of squashfs versions,
including 4.3 + lzma. You can find them on the
`DomoticX <http://domoticx.com/bestandssysteem-squashfs-tools-linux/>`__
website, lower down on the that page.


**My original post:**

In case you didn't know already (unless you're a multiplatform code
warrior, you probably didn't), the
`Squashfs <http://squashfs.sourceforge.net/>`__ tools have some problems
while being compiled under `Cygwin <http://cygwin.com/>`__. In fact,
they don't compile at all, mainly because a few lacking headers and
multiprocessor detection. Nevertheless, actually convincing them to
build isn't difficult at all.

To save you the extra work of doing so, I've created a patch, which can
be applied against the aforementioned 4.0 version of the
`squashfs-tools <http://sourceforge.net/projects/squashfs/files/squashfs/squashfs4.0/squashfs4.0.tar.gz/download>`__,
and I've made it available here: http://www.mediafire.com/?1txydxozzdo

If you're too lazy to patch and build your own, I've also uploaded the
binaries. These don't actually need Cygwin to be installed, as long as
the 2 .dll files remain in the same folder (or in the PATH) as the
executables. Get those from here (tar.gz archive):

http://www.mediafire.com/?yymd2mzlmnn


Enjoy!


**Edit:** Upon user request, I have also compiled and uploaded squashfs
3.0, 3.1 and 3.4, and their corresponding patches:

+-----------------------------------+-----------------------------------+
| File                              | Download Link                     |
+===================================+===================================+
| SquashFS 3.0 Cygwin               | `binaries                         |
|                                   | (tar.gz) <http://www.mediafire.co |
|                                   | m/file/mmger02tidw/squashfs_tools |
|                                   | -3.0-i686-cygwin.tar.gz>`__       |
|                                   | `patch <http://www.mediafire.com/ |
|                                   | file/zcdcnjd2fme/squashfs_tools-3 |
|                                   | .0-i686-cygwin.patch>`__          |
+-----------------------------------+-----------------------------------+
| SquashFS 3.1 Cygwin               | `binaries                         |
|                                   | (tar.gz) <http://www.mediafire.co |
|                                   | m/file/elcvdzdk2w1/squashfs_tools |
|                                   | -3.1-i686-cygwin.tar.gz>`__       |
|                                   | `patch <http://www.mediafire.com/ |
|                                   | file/hzmim3njtzw/squashfs_tools-3 |
|                                   | .1-i686-cygwin.patch>`__          |
+-----------------------------------+-----------------------------------+
| SquashFS 3.4 Cygwin               | `binaries                         |
|                                   | (tar.gz) <http://www.mediafire.co |
|                                   | m/file/oy3m0dml2d5/squashfs_tools |
|                                   | -3.4-i686-cygwin.tar.gz>`__       |
|                                   | `patch <http://www.mediafire.com/ |
|                                   | file/hjnmxgmjimn/squashfs_tools-3 |
|                                   | .4-i686-cygwin.patch>`__          |
+-----------------------------------+-----------------------------------+
| SquashFS 4.0 Cygwin               | `binaries                         |
|                                   | (tar.gz) <http://www.mediafire.co |
|                                   | m/file/yymd2mzlmnn/squashfs_tools |
|                                   | -4.0-i686-cygwin.tar.gz>`__       |
|                                   | `patch <http://www.mediafire.com/ |
|                                   | file/1txydxozzdo/squashfs_tools-4 |
|                                   | .0-i686-cygwin.patch>`__          |
+-----------------------------------+-----------------------------------+
