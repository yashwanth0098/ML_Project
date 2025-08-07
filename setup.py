from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requiremnts=[]
    with open(file_path) as file_obj:
        requiremnts=file_obj.readlines()
        requiremnts=[req.replace('\n','') for req in requiremnts]
        if '-e .' in requiremnts:
            requiremnts.remove('-e .')
    return requiremnts

setup(
    name='ml_project',
    version='0.0.1',
    author='Yashwanth ',
    author_email='yashwanth0098@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    # description='A machine learning project for prediction for classification'    
    
)