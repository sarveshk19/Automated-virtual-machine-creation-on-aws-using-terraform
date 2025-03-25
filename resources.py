#Generating vsphere resource
import json
import os
import sys
from python_terraform import *

fp = open("terraform.tf","a")

#Opening json files
def resource(fp):
    with open("C:\\Users\\SARVE\\Downloads\\vm_configuration.json") as json_file:
        inp = json.load(json_file)     
    fp.write('provider"aws"{\n')
    fp.write('region = "' + inp["region"] + '"\n')
    fp.write('}\n')
    fp.write('resource "aws_instance""my_instance" {\n')
    fp.write('ami = "' + inp["amiKey"] + '"\n')
    fp.write('instance_type = "' + inp["instanceType"] + '"\n')
    fp.write('count = "' + inp["numVMs"] + '"\n')
    fp.write('tags = {\n')
    fp.write('Name= "' + inp["name"] + '${count.index}"\n')
    fp.write('}\n}')
    
    json_file.close()