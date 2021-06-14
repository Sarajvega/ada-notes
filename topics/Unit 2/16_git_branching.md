# Branching in Git

## Vocab
- Branch: Git feature that captures a snapshot of code changes as one git commit history. 
  
## Branches
- The default name for the default branch is main
- Branches are created from another branch's commit. 
  - new branch and an old branch share the exact same commit history until the point that the branch is created and branches off.
- When we add commits to one branch, the commit isn't included in the Git histories of other branches.
- Merging branches results in two branches combining their Git histories. 
  -  branch-a into branch-b means merging the commit history of branch-a into the commit history of branch-b.
     -  We can merge main into click-button-feature.

Feature Branches:
- Designating one branch to represent the ultimate branch of "working" software, usually the main branch
- Agreeing that all active development and work-in-progress happens on branches other than main
- Each branch is dedicated to making commits solely for one feature at a time

When to use:
- Building a new feature and the tests for the new feature
- Modifying an existing feature and updating the tests for this feature
- Bug fixes
- Making small, isolated changes, such as fixing typos

Order of operations:
- We will first merge main into our feature branch, to handle any divergence in main that has happened while the feature work has been underway. 
- After resolving any merge conflicts and confirming our code is still working as expected, we will merge the feature branch back into main, so that main gets the unified, merged commit history.
- feature branch is deleted.

Experimental branches tend to take the approach of a "proof of concept." We give ourselves permission to write potentially messy code now, then write more intentional code (considering testing, readability, usability, and flexibility) later.

When we begin on such an endeavor, we should:
- Determine the goal of the exploration at the beginning.
- Create a time limit of less than one day.
- Decide to delete the branch at the end of the experiment, and create a separate new branch with clean commits after the research is over. This intentional step is to help us resist the temptation of including our exploratory code in our production code base.

## Create branches
When we create a branch, we should first and foremost be aware of our current location. In which branch are we currently working? What is the most recent commit?
`git status` tells us what branch we are on
`git branch` tells us how many brnaches there are and the * indicates which we are on. 
`git branch <new-branch-name>` creates a new branch that contains same commit history as branch we are on currently. 
`git switch <destination-branch-name>` switches the branch we are on to an exsiting branch.
- Can be 'unsafe'
- Git tries to preserve unstages changes/staged canges
  - Sometimes there isn't a way to preserve and git will ask we take action.
  - Do:
    - Create a commit with the unstaged and/or staged changes. This way, these changes will stay on the current branch before switching.
    - Use Git's stash feature, which will save unstaged and staged changes in the stash, instead of a commit.

`git checkout <destination-branch-name>` changes our location to another branch, older syntax.

if you want to create a new branch AND check it out at the same time, you can simply type `git checkout -b <yourbranchname>`
## Delete Branches
`git branch -d <branch-name>`


Work through the following sections of https://learngitbranching.js.org/  :

Introduction Sequence
Lessons 1, 2, and 3
Ramping Up
All lessons