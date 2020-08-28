from flask import Flask, request, render_template, jsonify 

import deepspeech as ds
import time
import uuid
import os
from constant import MODEL, SCORER
from python_client import speechToText

import threading
from queue import Queue, Empty


####### preload model ########################################################
print("Model load start")
start_model = time.time()
model = ds.Model(MODEL)
print("Model loaded : {}s".format(time.time()-start_model))

print("Scorer load start")
start_scorer = time.time()
model.enableExternalScorer(SCORER)
print("Scorer loaded : {}s".format(time.time()-start_scorer))
##############################################################################

app = Flask(__name__, template_folder='./templates/')

requests_queue = Queue()
BATCH_SIZE = 1
CHECK_INTERVAL = 0.1

def handle_requests_by_batch():
    while True:
        requests_batch = []
        while not (len(requests_batch) >= BATCH_SIZE):
            try:
                requests_batch.append(requests_queue.get(timeout=CHECK_INTERVAL))
            except Empty:
                continue

            for request in requests_batch:
                request['output'] = run(request['input'][0])

threading.Thread(target=handle_requests_by_batch).start()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/stt", methods=["POST"])
def stt():

    if requests_queue.qsize() > BATCH_SIZE: 
        return jsonify({'error': 'Too Many Requests'}), 429

    file_name = str(uuid.uuid4()) + '.wav'
    audio = request.files['audio']
    audio.save(file_name)
    
    req = {
        'input': [file_name]
    }

    requests_queue.put(req)
    while 'output' not in req:
        time.sleep(CHECK_INTERVAL)

    text = req['output']


    if os.path.exists(file_name):
        os.remove(file_name)

    if text == 500:
        print("real 500")
        return jsonify({'msg':'Server Error convert speech to text'}), 500

    return jsonify({'msg': text}),200

def run(audio):

    try:
        text = speechToText(model, audio)
    except:
        return 500

    return text

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=80)