from distutils.command.install import install
from re import L
from setuptools import find_packages, setup 
#this will automatically find all the packages in the entire machine learning application
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    """
    this function will return list of requirements
    """
    requirements_list = []
    with open(file_path) as file_obj:
        requirements_list = file_obj.readlines()
        requirements_list = [req.replace("\n","") for req in requirements_list]
        if HYPEN_E_DOT in requirements_list:
            requirements_list.remove(HYPEN_E_DOT) 
    return requirements_list

setup(
name = "end_to_end_ml_project",
version= "0.0.1",
author="avijit",
author_email="avijit.bhattacharjee1996@gmail.com",
packages= find_packages(),
install_requires = get_requirements("requirements.txt")

)