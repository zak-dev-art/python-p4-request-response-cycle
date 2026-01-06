#!/usr/bin/env python3

# Example 1: Basic request object usage
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    host = request.headers.get('Host')
    return f'<h1>The host for this page is {host}</h1>'

# Example 2: Adding current_app context
from flask import current_app

@app.route('/app-info')
def app_info():
    host = request.headers.get('Host')
    appname = current_app.name
    return f'''<h1>The host for this page is {host}</h1>
               <h2>The name of this application is {appname}</h2>'''

# Example 3: Using hooks and g object
import os
from flask import g

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/with-path')
def with_path():
    host = request.headers.get('Host')
    appname = current_app.name
    return f'''<h1>The host for this page is {host}</h1>
            <h2>The name of this application is {appname}</h2>
            <h3>The path of this application on the user's device is {g.path}</h3>'''

# Example 4: Custom status codes
@app.route('/accepted')
def accepted():
    return '<h1>Request accepted but not processed</h1>', 202

# Example 5: Using make_response
from flask import make_response

@app.route('/response-object')
def response_object():
    response_body = '<h1>Using make_response</h1>'
    status_code = 200
    headers = {'Custom-Header': 'Flask-Example'}
    return make_response(response_body, status_code, headers)

# Example 6: Redirect and abort
from flask import redirect, abort

@app.route('/redirect-example')
def redirect_example():
    return redirect('/')

@app.route('/error-example')
def error_example():
    abort(404)

if __name__ == '__main__':
    app.run(port=5556, debug=True)