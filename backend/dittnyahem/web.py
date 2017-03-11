import logging
from flask import Flask, request, Response, render_template, session, redirect, url_for, current_app
import flask
from gevent.pywsgi import WSGIServer
#from flask.ext.cors import CORS
logger = logging.getLogger(__name__)

def start_web(port, web_debug):

    app = Flask(__name__)
    #CORS(app)
    app.debug = web_debug
    app.secret_key = "a123123U36ewbsfbfb"

    @app.route("/")
    def index():
        logger.debug("Serving index")


        return render_template("index.html")

    logger.info("Starting web on %s", port)
    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()