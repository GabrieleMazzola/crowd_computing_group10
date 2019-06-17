import requests
import json
import random
from task1_creator import  get_instructions_task_1, get_cml_task_1

API_KEY = "_tvh3mg7NZCMMR-GyGG8"
ENDPOINT = "https://api.figure-eight.com/v1/jobs.json"
headers = {'content-type': 'application/json'}



if __name__ == '__main__':
    print("Starting the creation of the job...")

    with open(r"./data_task1.json") as f:
      info_json = json.load(f)
    
    instructions = get_instructions_task_1(info_json)
    cml = get_cml_task_1(info_json)

    payload = {
        'key': API_KEY,
        'job':{
            'title': info_json['job_title'],
            'instructions': instructions,
            'cml': cml
        }
    }
    
    response=requests.post(ENDPOINT, data=json.dumps(payload), headers=headers)
    print(response.content)

    print("Creation done.")

