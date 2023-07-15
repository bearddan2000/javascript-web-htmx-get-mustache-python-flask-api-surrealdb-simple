from flask import Flask, request
import logging
from client import Endpoint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def smoke_test():
    d = {'hello': 'world'}
    return {'results': d}

@app.route('/dog')
async def get_all():
    results = await endpoint.get_all()
    return {'results': results}

@app.route('/dog/breed/<string:breed>', methods=['GET', 'DELETE', 'POST'])
async def filter_del_upd_by_breed(breed: str):
    results = []
    if request.method == 'GET':
        results = await endpoint.filter_by('breed', breed)
    elif request.method == 'DELETE':
        results = await endpoint.delete('breed', breed)
    elif request.method == 'POST':
        results = await endpoint.update('breed', breed)
    return {'results': results}

@app.route('/dog/color/<string:color>', methods=['GET', 'DELETE', 'POST'])
async def filter_del_upd_by_color(color: str):
    results = []
    if request.method == 'GET':
        results = await endpoint.filter_by('color', color)
    elif request.method == 'DELETE':
        results = await endpoint.delete('color', color)
    elif request.method == 'POST':
        results = await endpoint.update('color', color)
    return {'results': results}

@app.route('/dog/my_id/<string:id>', methods=['GET', 'DELETE', 'POST'])
async def filter_del_upd_by_id(id: str):
    results = []
    if request.method == 'GET':
        results = await endpoint.filter_by('my_id', id)
    elif request.method == 'DELETE':
        results = await endpoint.delete('my_id', id)
    elif request.method == 'POST':
        results = await endpoint.update('my_id', id)
    return {'results': results}

@app.route('/dog/breed/<breed>/color/<color>', methods=['PUT'])
async def ins_by_breed(breed: str, color: str):
    results = await endpoint.insert(breed, color)
    return {'results': results}

if __name__ == "__main__":
    endpoint = Endpoint()
    app.run(host ='0.0.0.0', port = 5000, debug = True)
