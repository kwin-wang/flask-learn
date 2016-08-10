# from flask import render_template
# from flask.ext.mail import Message
# from config import config
# from . import mail
#
#
# def send_email(to, subject, template, config_name='default',  **kwargs):
#     cfg = config.get(config_name)
#     msg = Message(cfg.FLASKY_MAIL_SUBJECT_PREFIX + subject,
#                   sender=cfg.FLASKY_MAIL_SENDER, recipients=[to])
#     msg.body = render_template(template + '.txt', **kwargs)
#     msg.html = render_template(template + '.html', **kwargs)
#     mail.send(msg)


from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    #for k, v in app.config.items():
    #    print k, v

    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

#
# def send_email(to, subject, template, **kwargs):
#     app = current_app._get_current_object()
#     msg = Message(app.config.get('FLASKY_MAIL_SUBJECT_PREFIX') + subject,
#                   sender=app.config.get('FLASKY_MAIL_SENDER'), recipients=[to])
#     msg.body = render_template(template + '.txt', **kwargs)
#     msg.html = render_template(template + '.html', **kwargs)
#     mail.send(msg)