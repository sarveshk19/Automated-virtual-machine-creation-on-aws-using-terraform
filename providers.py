import json
import os
import sys
from python_terraform import *

fp = open("terraform.tf","a")

#Generating Provider Details from JOSN file 
def provider_details(fp):
    with open("providers.json") as json_file:
	    inp = json.load(json_file)
    
    temp=[]

    for pr in inp:
        temp.append(pr)
    provider = temp[0]

    fp.write('provider"aws"{\n')
    fp.write('region = "' + inp["aws"]["region"] + '"\n')
    fp.write('}\n')
 #   fp.write('access_key = "' + inp["aws"]["access_key"] + '"\n')
  #  fp.write('secret_key = "' + inp["aws"]["secret_key"] + '"\n')


    json_file.close()