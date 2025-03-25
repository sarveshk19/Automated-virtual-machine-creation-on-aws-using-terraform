#Generating terraform file
import json
import os
import sys
from python_terraform import *
import providers
import resources
import subprocess
import time
#Terraform Var
tf=Terraform()


#Opening json files
#with open("providers.json") as json_file:
	#inp = json.load(json_file)

with open("C:\\Users\\SARVE\\Downloads\\vm_configuration.json") as json_file2:
    typ = json.load(json_file2)


    #Terraform File creation
   
    #creating work directory
    fileDir = "terraform-1"
    filename = "terraform-1"+".tf"
    path = fileDir+"/"+filename
    if not os.path.exists(fileDir):
        os.mkdir(fileDir)
        if os.path.exists(path):
            os.remove(path)
            fp = open( path, "a")
        else:
            fp = open( path, "a")
    else:
        if os.path.exists(path):
            os.remove(path)
            fp = open( path, "a")
        else:
            fp = open( path, "a")

        #file population
        #providers.provider_details(fp)
        resources.resource(fp)
        fp.close()
        
        #Selecting Work Directory
        fileDir = "terraform-1"
        os.chdir(fileDir)
            
        

#### Terraform Commands ####

        #Terraform Init: Initializes terraform plugins
        print("\n####################################\nTerraform Init\n##########################################\n")
        start_time = time.time()
        tf.init(capture_output = False)
	    #Terraform Plan: Create an execution plan
        print("\n#######################################################\nTerraform Plan\n#######################################################\n")
        tf.plan(capture_output = False)

        
	    #Terraform Apply: Applies the execution plan
	    #print("\n#######################################################\nTerraform Apply\n#######################################################\n")
        #tf.apply(capture_output = False)
       # Replace with your actual Terraform command
        terraform_command = "terraform apply -auto-approve"
        # Run Terraform command from Python
        subprocess.run(terraform_command, shell=True)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time} seconds")
        os.chdir("..")

#json_file.close()
json_file2.close()