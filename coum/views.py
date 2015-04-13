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

