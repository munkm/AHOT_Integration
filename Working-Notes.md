### Overview
[Summary of building Sebastian's codes](#SSummary)
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
