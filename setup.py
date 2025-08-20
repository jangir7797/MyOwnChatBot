from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements from a file and returns a list of packages.
    """
    requirements = []
    with open(file_path) as file:
        for line in file.readlines():
            line = line.strip()
            if line and line != HYPEN_E_DOT:  # Ignore empty lines and -e .
                requirements.append(line)
    return requirements

setup(
name='MyOwnChatBot',
version='0.1.0',
description='An chatbot application',
author='Himanshu Jangir',
author_email='himanshujangir7797@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)