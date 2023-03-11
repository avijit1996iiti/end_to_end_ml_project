
# End to End Machine Learning Project 

This project is to create a general struture for all machine learning project. 


## Authors

- [@avijit1996iiti](https://www.github.com/avijit1996iiti)


## Github and Code Setup

#### Step1 
Create a new repo named end_to_end_ml_project in git

#### Step2
Crete a folder (ml_end_to_end) in local system where you will keep all code files

#### Step3
In the local folder just created, open the terminal and type “code .”. It will open a VS code instance. (provided you have already configured it) 

#### Step4
Create a new python environment by using the below commands (Here I am using Ubuntu 20.04) 

	sudo apt install python3-venv  # to install venv
     
	python3 -m venv ml_end_to_end   # to create a venv named  ml_end_to_end

	source ml_end_to_end/bin/activate   # activate the environment

#### Step5

Initialize a git repo in the local folder just created by using the below command

	git init

#### Step6
Create a README.md file in the local folder and add -> Commit ->set branch to main ->add remote origin ->push  to git using the below commands
	git add README.md

	git commit -m “first commit”

	git branch -M main

	git remote add origin 	https://github.com/avijit1996iiti/end_to_end_ml_project.git

	git push -u origin main
	(Here you need to authenticate your github account to vs code)

#### Step7
Create a .gitignore file in git with selecting python option 

#### Step8
Do a git pull to sync the repo

#### Step9
Add the cwd folder name in environments of .gitignore

#### Step10
Create a setup.py  and requirements.txt in local 
the setup script is the center of all activity in building, distributing and installing modules using the distutils. This will be responsible in creating machine learning application as a package 

#### Step11
Work on the setup.py file 

#### Step12
create a new folder named “src” and if you want src to be found as a package. Afterthat, create a “__init__.py” file in that folder   

#### Step13


    pip install -r requirements.txt
        