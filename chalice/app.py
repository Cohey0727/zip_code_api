import subprocess
from chalice import Chalice

app = Chalice(app_name='zip_code_api')


@app.route('/')
def index():
    return {'status': 'OK'}


@app.route('/zip_code/{zip_code}')
def hello_name(name):
    return {'hello': name}


@app.route('/initialize')
def hello_name(name):
    return {'hello': name}
