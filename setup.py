from setuptools import setup, find_packages
from typing import List

HYPEN = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements."""
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements=[req.replace('\n', '') for req in requirements]
        if HYPEN in requirements:
            requirements.remove(HYPEN)

    return requirements

setup(
    name='Hey',
    author='Sameeran',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)