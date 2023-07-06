# Git Training Exersizes.

This should just be a playground to play around with git concepts. It is
written in python, but that really shouldn't matter. You can do all of the
exercises with MD files if you would like. The key is to have a place where you
can freely change history and it doesn't matter.

## Exercise list
Anyone that claims to be a professional with Git should be able to do the
following:

1. Create a branch
2. Switch branches
3. Pull remote changes
4. Add commits
5. Amend commits
6. Remove (untrack) files
7. Rebase (use this instead of merge 99% of the time)
8. Cherry Pick
9. Manage conflicts during merge, rebase, or cherry-pick
10. Squash commits through interactive rebase, or reset and commit
11. Push changes
12. Force push when needed, and understand when it should be done and when not
13. Basics of creating a PR, roles of reviewers, and roles of requesters.

## Basic recommendations based on my experience

* Branch names should be descriptive, and when appropriate contain a ticket
    number or some identifier that goes back to your chosen work management
    system.
* Favor small feature branches that are short lived and only worked on by one
    person. This removes conflicts.
* If your trunk branch (main or master) changes often, rebase your feature
    branch. Favor rebase over merge, and don't mix the two. Rebasing removes
    your changes, applies all changes from the remote trunk, and then
    re-applies your changes. This keeps history cleaner, makes squashing and
    conflict resolution much easier.
* Commit messages should be useful, and describe what the code change is.
    Messages like "Got it working", "Did some stuff", etc. are not useful and
    make using the git history painful.
* Commit work in progress often. Using something like `WIP: ` before your
    commit message can help identify small commits that are candidates for
    squashing later.
* Squash commits into logical chunks of work. This helps with cherry picking,
    and reviewing history for when something has changed. This also lets you
    replace all the `WIP: ` comments with a collective set of comments on what
    was done.
* When you push your changes up, if you have rewritten history locally, so that
    local and remote are different, you will have to force push your changes. On
    short lived feature branches this is inconsequential, because the only
    remote changes are ones that you pushed on your branch.
* If your branch has any git hooks, like a pre-push hook, do not skip those
    when you run into a failure. This just pushes the failure farther down the
    line and to more team members. Avoid skipping checks.
* When you create a pull request do the following:
    * Assign the PR to yourself
    * As needed, use the draft PR. Only request other reviewers when no longer
        a draft.
    * Once you have requested a review, do not re-write history (rebase /
        squash / amend and then force push). Add new commits if changes are
        requested.
    * Consider squash and merge when merging into trunk. This can keep trunk
        history very clean and easy to cherry pick. If you are using git flow
        style branches, do not squash the commits from trunk into your long
        lived production branch.
* When you review a pull request do the following:
    * Do not review draft PR's.
    * Do not merge (unless you are specifically asked to by the requester)
    * Read every line of the PR. Look for sound logic, if that logic addresses
        the issue, are there tests, and do the tests actually test the logic
        written.
    * Add comments as needed in the PR. By adding comments here, it centralizes
        the conversation, and avoids spiralling DM's in chat systems that are
        in no way connected with the actual PR.
