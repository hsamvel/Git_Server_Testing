import git
import os
import sys
# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(os.path.realpath(sys.executable))
elif __file__:
    application_path = os.path.dirname(__file__)
print(os.path.dirname(application_path))
repo = git.Repo(application_path)
repo.git.reset("--hard")
repo.git.clean("-xdf")
git.Repo(application_path).remotes["origin"].pull()
