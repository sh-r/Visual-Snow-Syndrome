# Contributing to Visual Snow Syndrome Diagnostic
Thank you for taking time to contribute (or at least considering to). This is a community project.

Contribution does not necessarily mean you have to modify source code and fix a bug or add a new functionality. 
Reporting a bug using the [Issues](https://github.com/sh-r/Visual-Snow-Syndrome/issues) tab is also highly appreciated and a good way to start contributing to the project.

It is essential that you know how to use Git as well as GitHub. 
While the maintainers will be more than happy helping you make your first PR, prerequisite know-how makes it easier for everyone involved. 
Check this [guide](https://github.com/firstcontributions/first-contributions) if you've never contributed to a project on GitHub before.

Please note we have a Code of Conduct. Please follow it in all your interactions with the project.

When you submit code changes, your submissions are understood to be under the same [License](https://github.com/sh-r/Visual-Snow-Syndrome/blob/master/LICENSE) that covers the project. 
Feel free to contact the maintainers if that's a concern.

## Contributors Pull Request Checklist
1. Fork the repository and branch from development.

2. Work on your changes. Make sure you commit as frequently as required. Once you're done making the changes, push the commits to your fork. 
Checkout the Commit Messages section to find guidelines relating to commit messages.

3. If the changes you make fixes a bug in master or adds a new feature, note it down in the changelog.

4. Head over to the pull requests page and create a new pull request. Make sure that the PR is from your feature branch into this repo's development branch. 
If you are making changes that affect the UI in any way, attach an image in your PR description.

5. Wait for a maintainer to review your commit. If they find any issue (including redundant code, unnecessary changes, potential bugs), they will point it out to you. 
Make any necessary changes and push them to your fork. Ideally, try not to force push as it becomes harder for the maintainers to keep track of changes. 
Mark the review as resolved.
If everything looks okay, the maintainers will go ahead and merge your changes into the repo.

## Commit Messages
Proper commit messages (subject + body) is a very important aspect of any project. 
A good commit message communicates the exact details of the commit to other people without them having to go through the changes made.
The subject of a commit message should be:
1. capitalized
2. written in the imperative (e.g., "Fix ...", "Add ...")
3. kept short, while concisely explaining what the commit does.
4. clear about what part of the code is affected

Maintainers' Guide to Versioning


Note: Regarding master: master should always point to the latest release commit i.e a commit that updates the version number in the changelog and any other files. 
The commit that master points to should also be tagged with the version number of that release.

## Few Contribution Suggestions
We welcome any open source contributions you would like to make! Some of the improvements we thought of till now:
1. Adding more types of noise like gaussian, poisson, localvar, etc 
2. In the Linux executable file, the icon is not shown when opened in File Explorer though the --icon flag was set in PyInstaller.
3. An executable file compatible with MAC OS X
4. Making the noise continuously moving, sort of like an animation
5. Simulating nyctalopia, floaters, afterimages, etc
6. Taking in a saved image and using the saved text file to continue editing the same image 
7. Implementing stacks, i.e. Undo and Redo operations
8. Bug fixes
9. Maybe add the icon as a small window on startup of the application? I did spend a lot of time on the logo for it just to be really small xD.
