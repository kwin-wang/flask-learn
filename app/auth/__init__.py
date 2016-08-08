# -*- coding:utf-8 -*-
__author__ = 'yajun'
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views