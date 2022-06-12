## Machine_Learning_Project_1
Machine Learning Project

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)

### Open VS code via terminal:

folder_name/code .

### Inside VScode terminal window

Creating and activating conda environment
```
conda --version
```
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```

Create requirements.txt and then install the requirements
```
pip install -r requirements.txt
```

### Git Commands

To check git status
```
git status
```

> Note: Files or folders to be ignored must be added in .gitignore file

Add all files
```
git add .
```

Add single file
```
git add filename
```

To create version/Commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

Origin is nothing but the github repo url
To check remote url
```
git remote -v
```

To check all versions maintained by git
```
git log
```

To check branch name
```
git branch
```