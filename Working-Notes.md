### Overview
* [Summary of building Sebastian's codes](#SSummary)
* [Converting files from ifort to gnu](#gnu_build)


***
<a name="SSummary"/>
### Summary of building Sebastian's codes so far:
1) in 3D/lapack_dependency folder build lapack:
```
> ./cmpllpack
```
2) build codes (with icc-x86_64/intel-amd64 module loaded)

in each `src_*` folder (except 2D?) need to `> ln -s ../../lapack_dependency/lapack.a`

note: the executables are always placed one level up in the directory structure.

A. AHOTN/src_AHOTN_NEFD_gesv
```
> ./compile
```
compiles; creates ahotn_nefd.exe; work fine.

Same result with compile-h; debug makes ahotn_nefd; this works also.

B. AHOTN/src_LL
```
> ./compile
```
compiles; creates LL.exe; works fine.

`ifort -c -g -traceback -check all -fpe0 ll_module.f90` was missing from the debug script (it also didn't need the line with ahotn_kernel_module.f90 nor that file, so I removed them). After adding it,
```
./debug 
```
compiles; creates ahotn1_nefd; this works also.

 

C. AHOTN/src_LN
```
> ./compile
```
compiles; creates LN.exe;  works fine.

`ifort -c -g -traceback -check all -fpe0 lin_kernel_module.f90` was missing from the debug script (it also didn't need the line with ahotn_kernel_module.f90 nor that file, so I removed them). After adding it,
```
./debug 
```
compiles; creates ahotn1_nefd; this works also.

D. DGFEM/src_dgfem_complete_solver_dense
```
> ./compile
```
compiles; creates DGCTD.exe; works fine.

compile-h also works

idebug makes DGLA.exe, which also works

E. DGFEM/src_dgfem_lagrange_solver_dense
```
> ./compile
```
compiles; creates DGLAD.exe; works fine.

compile-h also works

idebug makes DGLA.exe again, which also works

F. DGFEM/src_LD
```
> ./compile
```
compiles; creates LD.exe; works fine.

compile-h,compileO0, compileO1, compileO2, and idebug also work (started saving outputs w diff compile extensions here)

G. SCT-Step/src_ahotn-step-sct
```
> ./compile
```
compiles; creates ahotn0-sct.exe; needs different input files - they're in test_inps/sct_step_test. This test works.

The debug version gives this compiler warning over and over:

forrtl: warning (402): fort: (1): In call to NORM, an array temporary was created for argument #1

H. 2D/src
```
> ./compile
```
compiles; creates ahot2d; works fine.


***
<a name="gnu_build"/>
### Converting files from ifort to gnu:

Process for converting each app from ifort to gnu:

First, change the compiler listed in the compile and debug scripts from ifort to gfortran. 

Also, remove the `-r8` flag.  gnu does not support that flag.  It forces everything to be done in double precision, which may cause errors later on.

We may have to go through the codes and verify that everything uses double precision.

Now, run the compile script in the apps directory;
```
    /compile
```
Look at the various errors produced, beginning with those that complain about GETARG:
```
    main.f90:28.31:
    CALL GETARG (1, infile, statin)
    Error: Too many arguments in call to 'getarg' at (1)
```
Locate the GETARG (usually in main.f90), and remove the last parameter.  You may have to comment out
error checking code that checks if the input files specified exist.  Might be good to add this in later.

Now, look at the errors that look similar to this:
```
    input.f90:97.43:
    IF (ex1 == .FALSE. .OR. ex2 == .FALSE. .OR. ex4 == .FALSE.) THEN
    Error: Logicals at (1) must be compared with .eqv. instead of ==
```
Locate and change the listed instances of `==` to `.eqv.`
Note:  Do not change any other instance of `==` you find.  Some should stay the same.

***

**Notes about compilers:**

- gfortran 4.4.7 and 4.5.3 are too old to compile SCT-step, but will compile AHOT and LN

- 4.6.4, 4.7.3, 4.8.1, 4.8.2, and 4.9.0 all work for SCT and AHOT (I checked all for SCT, only some for AHOT)

- with 4.9.0 running the SCT version of the test gives and error: 
```
Note: The following floating-point exceptions are signalling: IEEE_UNDERFLOW_FLAG IEEE_DENORMAL
```
This appears to be because of a patch implemented that was perhaps first released in this version? See [this](https://gcc.gnu.org/ml/fortran/2013-06/msg00072.html) and [this](https://gcc.gnu.org/ml/fortran/2013-06/msg00098.html). I think it's more fully implementing the fortran 2003 standard. The error info can be understood here. I think we can disable it on compile, but the warning seems valuable. 

 

** the default gfortran on Bk is too old **
to use the version that I built, add
```
export LD_LIBRARY_PATH=/usr/local/exnihlo/vendors/gcc/gcc-4.8.2/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/exnihlo/vendors/gcc/gcc-4.8.2/lib64:$LD_LIBRARY_PATH
export PATH=/usr/local/exnihlo/vendors/gcc/gcc-4.8.2/bin/:$PATH
```
to your bashrc file. 