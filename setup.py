from setuptools import find_packages,setup
from typing import List
HYPhen_E_DOR='-e .'

def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements ]

        if HYPhen_E_DOR in requirements:
            requirements.remove(HYPhen_E_DOR)
    
    return requirements

setup(
name="mlproject",
version='0.0.1',
author="animesh",
auhtor_email="animeshhazarika58@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
