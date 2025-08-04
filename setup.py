from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    """this function return the list of requirements"""
    requirement_lst:list[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Harshit Joshi",
    author_email="harshitjoshi769@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)    