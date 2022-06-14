## Machine_Learning_Project_1
Machine Learning Project

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)

### Open VS code via terminal:

- folder_name/code .

### Inside VScode terminal window

- Creating and activating conda environment
```
conda --version
```
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```

- Create requirements.txt and then install the requirements
```
pip install -r requirements.txt
```

### Git Commands

- To check git status
```
git status
```

> Note: Files or folders to be ignored must be added in .gitignore file

- Add all files
```
git add .
```

- Add single file
```
git add filename
```

- To create version/Commit all changes by git
```
git commit -m "message"
```

- To send version/changes to github
```
git push origin main
```
> Note: Origin is nothing but it indicates the github repo url

- To check remote url
```
git remote -v
```

- To check all versions maintained by git
```
git log
```

- To check branch name
```
git branch
```

### To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = 
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-reg-app

- BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase. Tag name can be anything, usually we use - latest

- To list docker image (get image id)
```
docker images
```

- Run docker image
```
docker run -p 5000:5000 -e PORT=5000 IMAGEID
```
- After substituting the image id
```
docker run -p 5000:5000 -e PORT=5000 2e0091f88131
```
- http://localhost:5000/

- To check running container in docker
```
docker ps
```

- Tos stop docker conatiner
```
docker stop <container_id>
```