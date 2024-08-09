import os
import pathlib
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]:%(message)s:')

project_name = "text_suumerization"

list_of_files = [
".github/workflows/.gitkeep", #using for cicd related deployment (for comit itakes youre code automatically)(gitkeep= empty folder cant be comited)
f"src/{project_name}/_init_.py",#(init_py constructer file installed as local packege to import stuff from folders,local packages need constructor file)
f"src/{project_name}/components/_init_.py",
f"src/{project_name}/utills/common_.py",#utility related code over here
f"src/{project_name}/logging/_init_.py",
f"src/{project_name}/config/_init_.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/pipeline/_init_.py",
f"src/{project_name}/entity/_init_.py",
f"src/{project_name}/constants/_init_.py",
"config/cofig.yaml",
"params.yaml",#store model related parameters
"app.py",
"main.py",
"Dockerfile",
"requirments.txt",
"setup.py",
"research/trial.ipynb",
]


for filepath in list_of_files:
	filepath = Path(filepath) #handle diffrence between windows and linux path
	filedir, filename = os.path.split(filepath) #get filename from path
	if filedir != "":
		os.makedirs(filedir, exist_ok=True)
		logging.info(f"creating directory: {filedir} for the file {filename}")
		
	if(not os.path.exists(filepath) ):
		with open(filepath, 'w') as f :
			pass
		logging.info(f"creating empty file {filepath}")
	else:
		logging.info(f"{filename} is already exists")	
	
	
