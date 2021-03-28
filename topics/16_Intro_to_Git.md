
# Intro to Git
### Vocab
Version: Code at a specific point in time labeled with an um based indentifier.
Version Control System: A tool that records file changes.
Git: A distributed version control system that mmakes snapshots of files whcih can be referenced later.
Repo: Directory
Commit: A change to files identified with a hash. 

Git vs Github: Git is the version control system we use. Git is a tool and we use this tool in the command line or IDE. GitHub is a service that hosts our codebases.

Git helps us:
- Version our software with commits and look at our commit history
- Collaborate with others

## Software is built as a history
VCS lets us understand what software is built over time. Git can track all files in a project. Commits are history snapshots that contain a lot of info including:
1. A summary of lines of code that were added, deleted, or changed, compared to the last commit
2. A way to refer to the last commit, or its "parent" commit
3. A unique ID for the commit, often called the commit hash
4. A commit message, a string describing the contents of the commit
5. The date and time that the commit was made

Every codebase a team collaborates on will have a repo. The repo is sotred on a hosting site. Every contributing dev needs access to the code and does so by cloning that repo. Each dev writes codes and gets updates from their teams and makes some commits. 

## Git Setup 
Fork: A repo that is based on another repo
Forking a repo: the act of making a forked repo from a base repo. 
Clone: A directory that contains a repo's code and Git history, and can keep track of the remote repo it's a clone of. 

To turn a folder into a git project:
`git init` which creates a hidden .git folder in the project's root. 

## Fork an exisitng project
When developers see a repo that would be a good base for a project, and the developer wants to remix this project for themselves, they can fork it.

**When to fork?**
1. When a dev needs copy of this git history
2. when they need more ownership/access 
3. To separate from the original repo

## Clone to your computer
Cloning creates a new folder on the local computer. This folder has the same name as the remote repo. Also, this folder contains all of the remote repo's current folders, files, and Git history.

**When to clone?**
When they needs things in the repo's code. 

## Commits
We refer to the collection of differences between two resources, such as files or versions, as a diff. A VCS can display a set of changes as a diff, allowing us to confirm our modifications before committing to our repo, or to review modifications made by others on our team.

**Best commits are small, focused on meaningful change, not a work in progress.**

When to commit?
- After implementing the code to make one test pass
- After writing one test and implementing the feature to make that test pass
- Before implementing a different feature
- After writing one or two functions
- After beginning to make a class
- After making function stubs, class stubs, or new files
- Before beginning to refactor code
- After refactoring one area of code

## Local and Staging Areas
Git allows us to be selective about the changes that go into a commit. It does this by providing two areas we can use to categorize them: the local changes area and the staging area.

Local changes area: for new code changed that only exist on this local machine.
Staging area: code changes that the dev intends to commit

To view changes in locan and staging areas: `git status`
Which gives:
- changes to be committed ( moved from local to staging). To unstage `git restore --staged <file>...`
- changes not staged for commit which describes local changes area/new code changed from tracked files.
- uUntracked filed: These are the files that Git understands are new and untracked, but the changes can't go into local changes until it's tracked

## Move Changes to Staging Area
- use `git add`
- `git add -p`: starts an interactive mode where local changes will be presented on screen one at a time. 

## Untracked Changes
When a new file is created in a project, it is untracked. No matter how many times we change its contents, Git won't store the different versions of an untracked file.

To track a new file: `git add <relative-path-to-untracked-file>`

## Commits Are Made After Local and Staging
We create a commit after our intended changes are in staging.
Commit with: `git commit -m "message"` 

Good commit messages:
- short; can be a sentence fragment, a sentence, or two
- accurate
- specific
- starts with a verb
- finishes the sentence, "When we apply this commit, this commit will..."

## Merge, Fetch, Pull
A repo that holds a codebase and commit history that is accessible to multiple team members is called a remote repository.
When we clone a repo from a remote host, Git gives a default nickname of origin to the site from where the repo was downloaded.
- `git fetch`: local machine needs to recognize that there are updates from another repo
- `git merge`: The two Git histories need to merge together, and become one using timestamps histories and commiting them in order. When more than 1 member cods a file, git will need to do a follow up commite to finalize the merge order. 
- `git pull`: fetch and merge in one. 

## Push to `Origin`
`git push` makes our changes available to the rest of our team. 
Git requires a local repo to pull changes and to be up-to-date with the remote repo, before pushing to the remote repo.

## Workflow
1. Confirm that the project is in the state you expect with `$ git status`
2. Determine what your next task or goal is.
3. Start running tests, writing code, etc.
4. When you have a small, meaningful change, get ready to make a commit:
   1. Move the intended changes from local changes area to staging with `$ git add`
   2. Create a commit and a commit message from the changes in staging with `$ git commit -m ""`
   3. Review the commit with `$ git show`
5. Create at least one commit. Continue to write code and make commits.
6. Fetch and merge any new commits from origin with $ git pull
7. Review the code; check that the tests still pass, and the code still runs...If the code is broken, restart this process and make commits that will fix the problem
8. Send all of your commits to origin with `$ git push`
9. Review your work with `$ git status` and `$ git log`

## Reviewing Git Histories
Use `git status` all the time:
- To verify what changes are untracked, in local, and in staging
- Before moving changes from local area to staging area
- Before moving changes from the staging area to a commit
- After making a commit to witness the changes in the staging area disappearing

The command `$ git diff` outputs a summary of all changes in the local changes area. Use before moving changes from local area to staging are, seeing what changes you've written and deleted since last commit. 

Git commands that need to present more than a screensworth of data often show their results using a program called less. Scroll up/down with arrows or k/j. Spacebar to scroll by one page. b to scroll up by one page and q to exit. 

`diff --staged` reveals all staged changes. 

`git log` shows all commits made on this branch.

`git show` shows the details of a single commit. 
- The commit hash (ID)
- The author(s)
- The date and time that the commit was made
- The commit message
- The entire diff of that commit
