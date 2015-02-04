#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys

from flask import Flask, request, session, g, redirect, url_for, abort, \
                           render_template, flash



template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

UPLOAD_FOLDER = "./coum/static/imgs/"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

coum = Flask(__name__, template_folder = template_dir)

coum.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
coum.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

from coum import views

