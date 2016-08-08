from flask import render_template
from flask.ext.mail import Message
from config import config
from . import mail

def send_email(to, subject, template, config_name,  **kwargs):
    cfg = config.get(config_name)
    msg = Message(cfg.FLASKY_MAIL_SUBJECT_PREFIX + subject,
                  sender=cfg.FLASKY_MAIL_SENDER, recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)