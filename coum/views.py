#!/usr/bin/env python2
# -*- coding:utf-8 -*-

import os
import sys

from flask import Flask, request, session, g, redirect, url_for, abort, \
                  render_template, flash
from jinja2 import TemplateNotFound
from werkzeug import secure_filename

from coum import coum

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in coum.config['ALLOWED_EXTENSIONS']

@coum.route('/')
@coum.route('/index')
def index():
    """generates index page"""

    title = "cartooning"
    try:
        return render_template("index.html", title = title)
    except TemplateNotFound:
        abort(404)

@coum.route('/upload', methods=['GET', 'POST'])
def upload():
    """upload image by drag"""

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(coum.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index', filename=filename))

'''
@coum.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(coum.config['UPLOAD_FOLDER'],
                                               filename)
'''
