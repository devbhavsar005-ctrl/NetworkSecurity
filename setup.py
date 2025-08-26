from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
        this function is used to download all the reqi=uirements 
    """

    requirements_list:list[str]=[]
    try:
        with open("requirements.txt","r") as file:
            lines=file.readline()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement !="-e .":
                    requirements_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file is not found")

    return requirements_list



setup(
    name="Network_security",
    version="0.0.1",
    author="Dev Bhavsar",
    author_email="devbhavsar005@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements()
)