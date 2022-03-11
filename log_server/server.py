from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import yaml
import logging
import random
from logging.handlers import TimedRotatingFileHandler

from flask import Flask, redirect, url_for, request
import logging

logging.basicConfig(filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

location = [
    'us-east', 'us-east2', 'us-west', 'us-west2', 'can1', 'aus', 'london', 'beijing', 'mumbai', 'qatar', 'osaka',
    'berlin', 'paris', 'rio', 'st-petersberg', 'seoul', 'bangalore', 'sgp'
]

microservice = [
    'user-interface', 'application-backend', 'service1', 'service2', 'background-service'
]

status300 = [
    '300', '301', '302', '303', '304', '305', '306'
]

status400 = [
    '400', '401', '403', '404', '405' 
]

status500 = [
    '500', '502', '503', '504'
]

app = Flask(__name__)




@app.route('/endpoint1', methods = ['POST', 'GET', 'PUT'])
def endpoint1():
    # Endpoint 1 returns 200 series success reponses
    loc_pos = random.randint(0,17)
    mic_pos = random.randint(0,4)
    log_type = random.randint(0,9) # 10% chance of error, 30% chance of warning 70% info logs
    if request.method == 'GET':
        if log_type < 7:
            logging.info('"GET /endpoint1 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - 200')
        else:
            logging.warning('"GET /endpoint1 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - 200')
        return  'GET endpoint1'
    elif request.method == 'POST':
        if log_type < 7:
            logging.info('"POST /endpoint1 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - 200')
        else:
            logging.warning('"POST /endpoint1 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - 200')
        return  'POST endpoint1'
    else:
        if log_type < 7:
            logging.info('"PUT /endpoint1 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - 200')
        else:
            logging.warning('"PUT /endpoint1 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - 200')

        return  'PUT endpoint1'

@app.route('/endpoint2', methods = ['POST', 'GET', 'PUT'])
def endpoint2():
    # Endpoint 2 returns 300 series errors from the client side
    loc_pos = random.randint(0, 17)
    mic_pos = random.randint(0, 4)
    sta_pos = random.randint(0, 6)
    log_type = random.randint(0,9)
    if request.method == 'GET':
        if log_type < 6:
            logging.info('"GET /endpoint2 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status300[sta_pos]))
        elif log_type >= 6 and log_type < 9:
            logging.warning('"GET /endpoint2 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status300[sta_pos]))
        else:
            logging.error('"GET /endpoint2 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status300[sta_pos]))
        return  'GET endpoint2'
    elif request.method == 'POST':
        if log_type < 6:
            logging.info('"POST /endpoint2 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status300[sta_pos]))
        elif log_type >= 6 and log_type < 9:
            logging.warning('"POST /endpoint2 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status300[sta_pos]))
        else:
            logging.error('"POST /endpoint2 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status300[sta_pos]))
        return  'POST endpoint2'
    else:
        if log_type < 6:
            logging.info('"PUT /endpoint2 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status300[sta_pos]))
        elif log_type >= 6 and log_type < 9:
            logging.warning('"PUT /endpoint2 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status300[sta_pos]))
        else:
            logging.error('"PUT /endpoint2 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status300[sta_pos]))

        return  'PUT endpoint2'

@app.route('/endpoint3', methods = ['POST', 'GET', 'PUT'])
def endpoint3():
    # Endpoint 2 returns 300 series errors from the client side
    loc_pos = random.randint(0, 17)
    mic_pos = random.randint(0, 4)
    sta_pos = random.randint(0, 4)
    if request.method == 'GET':
        logging.info('"GET /endpoint3 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status400[sta_pos]))
        return  'GET endpoint2'
    elif request.method == 'POST':
        logging.info('"POST /endpoint3 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status400[sta_pos]))
        return  'POST endpoint2'
    else:
        logging.info('"PUT /endpoint3 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status400[sta_pos]))
        return  'PUT endpoint2'

@app.route('/endpoint4', methods = ['POST', 'GET', 'PUT'])
def endpoint4():
    # Endpoint 2 returns 300 series errors from the client side
    loc_pos = random.randint(0, 17)
    mic_pos = random.randint(0, 4)
    sta_pos = random.randint(0, 3)
    if request.method == 'GET':
        logging.info('"GET /endpoint4 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status500[sta_pos]))
        return  'GET endpoint2'
    elif request.method == 'POST':
        logging.info('"POST /endpoint4 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status500[sta_pos]))
        return  'POST endpoint2'
    else:
        logging.info('"PUT /endpoint4 HTTP/1.1" - "'+str(location[loc_pos])+'" - "'+str(microservice[mic_pos])+'" - '+str(status500[sta_pos]))
        return  'PUT endpoint2'



if __name__ == '__main__':
   app.run(debug = True)