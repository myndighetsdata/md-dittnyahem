import logging
from flask import Flask, request, Response, render_template, session, redirect, url_for, Blueprint, jsonify
import flask
import json
from gevent.pywsgi import WSGIServer
#from flask.ext.cors import CORS

from ams import AmsClient

logger = logging.getLogger(__name__)


def start_web(port, web_debug):

    app = Flask(__name__, static_url_path="")
    #CORS(app)
    app.debug = web_debug
    app.secret_key = "a123123U36ewbsfbfb"

    client = AmsClient()

    @app.route("/")
    def index():
        return render_template("test.html")

    @app.route("/search", methods=["POST"])
    def search():
        workGroups = [1, 2, 3]

        sr = client.search()


        return render_template("result.html", sr=sr)

    logger.info("Starting web on %s", port)
    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()