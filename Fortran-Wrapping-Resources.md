### Resources
* [f2py](#f2py-Resources)
* [fortran to c++](#c++wrap)
* [fwrap](#fwrap)

<a name="f2py-Resources"/>
### f2py Resources

A few f2py resources that will be useful for wrapping: 

- links to user's guide and an FAQ; the "Main Features" section is useful: [http://cens.ioc.ee/projects/f2py2e/](http://cens.ioc.ee/projects/f2py2e/)

- user guide/manual: [ http://cens.ioc.ee/projects/f2py2e/usersguide/index.html]( http://cens.ioc.ee/projects/f2py2e/usersguide/index.html) (follow the quick and smart way directions)

- directions from Fernando (a friend who works down the street; skip the email bit at the top): [http://cens.ioc.ee/pipermail/f2py-users/2003-April/000472.html](http://cens.ioc.ee/pipermail/f2py-users/2003-April/000472.html)

Fernando refers to the reference that I've attached below (the link in his post no longer works). 

- references (some of the talks might be helpful): [http://www.f2py.com/home/references](http://www.f2py.com/home/references)

- example, medium useful: [http://websrv.cs.umt.edu/isis/index.php/F2py_example](http://websrv.cs.umt.edu/isis/index.php/F2py_example)

- more directions and examples via scipy, go to f2py section of page: [http://docs.scipy.org/doc/numpy/user/c-info.python-as-glue.html](http://docs.scipy.org/doc/numpy/user/c-info.python-as-glue.html)

- example in sage (somewhat useful, has how to use blas and lapack): [http://www.sagemath.org/doc/numerical_sage/f2py.html](http://www.sagemath.org/doc/numerical_sage/f2py.html)

- scipy cookbook (not super useful): [http://wiki.scipy.org/Cookbook/F2Py](http://wiki.scipy.org/Cookbook/F2Py)

- api documentation: [http://f2py.sourceforge.net/docs/](http://f2py.sourceforge.net/docs/)

***
<a name="c++wrap"/>
### Wrapping with C++ 

Option 1: Wrapping fortran with c++ via auto generation python script. 
http://fortwrap.sourceforge.net/ 
License: MIT

Option 2: 
http://wwwasd.web.cern.ch/wwwasd/cernlib/cfortran.html 

License: 

THIS PACKAGE, I.E. CFORTRAN.H, THIS DOCUMENT, AND THE CFORTRAN.H EXAMPLE 
PROGRAMS ARE PROPERTY OF THE AUTHOR WHO RESERVES ALL RIGHTS. THIS PACKAGE AND 
THE CODE IT PRODUCES MAY BE FREELY DISTRIBUTED WITHOUT FEES, SUBJECT TO THE 
FOLLOWING RESTRICTIONS: 
- YOU MUST ACCOMPANY ANY COPIES OR DISTRIBUTION WITH THIS (UNALTERED) NOTICE. 
- YOU MAY NOT RECEIVE MONEY FOR THE DISTRIBUTION OR FOR ITS MEDIA 
(E.G. TAPE, DISK, COMPUTER, PAPER.) 
- YOU MAY NOT PREVENT OTHERS FROM COPYING IT FREELY. 
- YOU MAY NOT DISTRIBUTE MODIFIED VERSIONS WITHOUT CLEARLY DOCUMENTING YOUR 
CHANGES AND NOTIFYING THE AUTHOR. 
- YOU MAY NOT MISREPRESENTED THE ORIGIN OF THIS SOFTWARE, EITHER BY EXPLICIT 
CLAIM OR BY OMISSION. 

Cons: 
would require linking (in make file) to be established between the fortran files and interfacing c files.

***

<a name="fwrap"/>
### Fwrap
Fortran wrapping library:

Fwrap. located here:

http://fortrancython.wordpress.com/ and here http://fwrap.sourceforge.net/

Notes on building and using fwrap:

VERY IMPORTANT: VERSION OF NUMPY INSTALLED MUST PREDATE 1.8.0! Support for numpy scons was removed as indicated by this pull request on numpy's github:

  https://github.com/numpy/numpy/pull/2914
 
fWrap is dependant on numpy.scons, a sub library used in numpy that was removed as of numpy version 1.8. In order to be able to use fWrap, you must have numpy 1.7.$ installed. Below is a link to a linux distribution of 1.7.0:
 
  http://sourceforge.net/projects/numpy/files/NumPy/1.7.0/numpy-1.7.0.tar.gz/download
 
Instructions:
  1. type `pip uninstall numpy`
  for some reason, if numpy is not manually removed, reinstalling with a lesser version will not overwright the binary. Theirfore, before installing the outdated version you must remove the new.
     [if using anaconda: `conda remove numpy`]
  2. install numpy 1.7.0 from source with:
     `python setup.py install build`
     (I did `python setup.py build --fcompiler=gnu95` to make sure it used gfortran)
  3. install fWrap from source using directions below
 
IMPORTANT:  Must install fwrap from NEW source.. not listed on blog.  Github repository has not been updated since 2010.
    https://github.com/kwmsmith/fwrap/blob/master/INSTALL.txt
  NEWER SOURCE (use this one): (updated in 2010)
    https://bitbucket.org/kwmsmith/fwrap-dev

(Note: if you installed Python with Anaconda, you might already have fwrap. Was this one built properly?)

Installation instructions:

1) get f2py from googlecode:
```
  $ hg clone https://f2py.googlecode.com/hg/ f2py
  in the f2py folder:
  $ ./setup.py build
  $ ./setup.py install
```
  (not sure if these steps are needed or not?)

2) get fwrap-dev
```
  $ hg clone https://bitbucket.org/kwmsmith/fwrap-dev
```
3) put a symbolic link from the f2py/fparser package in
fwrap-dev/fwrap/ directory.
```
  $ cd /path/to/fwrap-dev/fwrap
  $ ln -s /path/to/f2py/fparser 
  $ cd ../ 
  $ python setup.py install
  $ python runtests.py -vv --fcompiler=gnu95 --no-cleanup 
    (note: Rachel fails 7 tests)
```
4) add fwrapc to your path if you don't already have it


Wrapping complie flags:
  `fwrapc source.f90 --build --name=one_arg --fcompiler=gnu95 --f90exec=/usr/bin/gfortran-4.8 -L/usr/lib/gcc/x86_linux-gnu/4.8.2 -lgfortran`

[for rachel: `fwrapc source.f90 --build --name=one_arg --fcompiler=gnu95 --f90exec=/usr/bin/gfortran-4.6 -L/usr/lib/gcc/x86_linux-gnu/4.6.3 -lgfortran`]

