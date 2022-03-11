# File primarily exists to ping the sever regularly and generate logs that would be written to the file specified.
import requests
import random
import time

url = "http://127.0.0.1"
port = "5000"
endpoints = ['endpoint1', 'endpoint2', 'endpoint3', 'endpoint4', 'endpoint5']
while True:
    m_count = random.randint(0,2)
    e_count = random.randint(0,4)
    time_sleep = random.random()*10
    if m_count == 0:
        data = requests.get(url+":"+port+"/"+endpoints[e_count]).json
    elif m_count == 1:
        data = requests.post(url+":"+port+"/"+endpoints[e_count]).json
    else:
        data = requests.put(url+":"+port+"/"+endpoints[e_count]).json
    time.sleep(time_sleep)
    print(data)