#!/usr/bin/env python2

import os
import sys

import flask
app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>coum<h1> \
           <h3>image cartoonizer<h1>'

if __name__ == "__main__":
    app.run()
