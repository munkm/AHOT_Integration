### Resources
* [f2py](#f2py-Resources)
* [fortran to c++](#c++wrap)

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

