from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from ..models import User

# @main.route('/', methods=['GET', 'POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#
#         # Note: different use with app
#         return redirect(url_for('.index'))
#     return render_template('index.html',
#                            form=form,
#                            known=session.get('known'),
#                            current_time=datetime.utcnow())


from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')
