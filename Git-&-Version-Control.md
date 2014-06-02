### Initial Setup:
(note: this is with `git@github.com:pyne/pyne.git` set as the `upstream` remote and `git@github.com:rachelslaybaugh/pyne.git` set as the `origin` remote)

make sure everything is up-to-date: `git pull upstream staging`

add Josh as a remote:  `git remote add howland git@github.com:howland/pyne.git`

check that this worked:  `git remote -v`

get Josh's repo:  `git fetch howland`

checkout our "master" branch created by Josh:  `git checkout transport `

add it to your online repo:  `git push origin transport` (check your page and make sure that you created that branch; don't forget to refresh the page :) )

make your own version of the branch; this should now be tracking the one Josh made:  `git branch transport-rnsdev`

checkout your new branch:  `git checkout transport-rnsdev` (name it appropriately)

add it to your online repo:  `git push origin transport-rnsdev` (check your page and make sure that you created that branch)
 

Josh: you'll only need to create a development branch. Your job with the main transport branch is to periodically pull in updates from pyne staging branch to keep us from diverging from it too far. 

### Pull Request / Merge management:
Example of Josh making a pull request to transport from transport-josh-dev with a remote `howland` setup as `git@github.com:howland/pyne.git`

get Josh's materials: `git fetch howland`

checkout the branch with the pull request and name it something temporary for testing (in this case the apt tmpdev): `git checkout -b tmpdev howland/transport-josh-dev` 

Poke around the code and make sure it's okay. If it is, you can merge the pull request on git hub or 

switch to the main transport branch: `git checkout transport`

merge the temporary brange into it: `git merge tmpdev`

push those changes up to the website: `git push origin transport`

Then you can delete the tmpdev branch.

If you need to make changes: on your tmpdev branch

change the appropriate things and git commit them

push your temporary branch to git hub: `git push origin tmpdev`

on github, initiate a pull request to `howland/transport-josh-dev` from `username/tmpdev`

The initiator of the pull request can merge in those changes, update anything else, and then you can repeat the fetching until everything is ok.


###What to version control:
text based files that we want to track the changes in: 

- source code (all .f90 or .py files, etc.)

- documentation and instructions

- input files

- support files (like the mat.dat file)

###What not to version control:
- executables (unless there's a strong need for this)

- all the files that are generated when you build stuff (e.g. object files, .pyc files, log files, etc.)

- output files (unless they're being used as a specific example
