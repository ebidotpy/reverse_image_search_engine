import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "reverseImageSearchEngine"

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    "App/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "reports/figures/.gitkeep", 
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "main.py", 
    "Dockerfile",
    "research/trials.ipynb",
    "README.me"

]
for filepath in list_of_files:
    filedir, filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creationg empty file: {filename}")
    else:
        logging.info(f"{filename} is already created")
        