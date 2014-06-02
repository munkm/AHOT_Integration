Timeline:

Task 1: determine wrapping strategy (timeline 1st wk) 
- must get buy-in by pyne-dev

Task 2: filestructure plan (timeline 1st wk) 
- must get buy-in by pyne-dev

Task 3: detailed implementation plan (timeline 2nd week)

Task 4: implement (timeline weeks 3-8) 
- document as you go 
- test as you go

Task 5: example of use (timeline week 9)

Task 6: pull request (do a dance!)


***

Initial goal: be able to run at least one of Sebastian's codes through Python given appropriate input files.

near-term goal: 
- input created in Python and given to a PyNE interfact to ahton 
- create a processing tool that reads the output file and creates a PyNE data structure for output manipulation (we need to determine a flux canonical form). 
- ability to return flux directly to PyNE?

Medium-term goal: deeper incorporation into PyNE. The first steps to do this are:

1. incorporation of PyNE mesh instead of getting mesh from input file 
2. incorporation of PyNE materials and nuclear data instead of getting data from input file

** associated issues ** 
- better error checking/handling 
- combining all the separate codes into one such that we don't have so much repeated code! 
- ability to generate source, boundary, and weight files

(unclear if we will pursue these next items, but this seems like a good place to record the thoughts)

Long-term goal: plug-and-play solvers (essentially develop all of the other parts and pieces s.t. all we really use is the sweep structure from the AHOT collection. 
- build quadratures in PyNE that can be used 
- build source specification utilities 
- build boundary condition specification utilities 
- add criticality calculation functionality (?legal issues?) 
- add ability to create and use preconditioners

Very long-term goal: parallelization?

***

Pyne Github branch for work: 
[https://github.com/howland/pyne/tree/transport](https://github.com/howland/pyne/tree/transport)

(see git directions below or click link on the right)

PyNE developer's guide: [http://pyne.io/latest/devsguide/index.html](http://pyne.io/latest/devsguide/index.html)
