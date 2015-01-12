#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys

from flask import Flask, request, session, g, redirect, url_for, abort, \
                           render_template, flash


template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

coum = Flask(__name__, template_folder = template_dir)

from coum import views

