StampProject
============




=============
Here's a quick summary of git if you forget some things
=============

Brian, there are two folders on the master branch. One "BrianProject" is your original project. Two "TroyProject"
has got my files and models that help demo some python stuff.

There are also two branches I created, BrianChanges and TroyChanges. If you were to run:

Currently, all three branches are the same.

So if you were to run:

git checkout BrianChanges

you will have a copy of your project. Now you can make changes on your files. As you do, git will track them. If you
like your changes, you can synchronize them with your copy on the cloud so that I can see them too.

If you run

git status

you will see all the files that have changed between your copy on your USB and the copy on the cloud. Git
allows you decide which of the files you want to synchronize with the cloud. You choose by running

git add $PATH_TO_FILE (where $PATH_TO_FILE could look something like ./TroyProject/main.py)

Then once you have added all the files you would like to synchronize with git, you will run

git commit

This will open a text editor so you can add a message to your commit. This is required. A simple message just
outlines the broad scope of what your commit accomplishes. ex: Created Filter Class

If you want to simplify this step, run

git commit -m "Created Filter Class" (m stands for message)

A commit packs together all the files in a neat little bundle which git keeps track of. Really handy. Now you can run

git push

Which will take all your commits since your last push and send them up to the cloud.


CATCH:
When you call git push, it will fail if I have changed a file on YOUR SAME BRANCH and it no longer matches your
old copy of the file. So this is why we each have our own branch. We can each change our own copy of the files,
then we can combine them all at the end. To make this easy though, I will only ever push to the branch TroyChanges.

