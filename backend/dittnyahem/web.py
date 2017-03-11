import logging
from flask import Flask, request, Response, render_template, session, redirect, url_for, current_app, jsonify
import flask
import json
from gevent.pywsgi import WSGIServer
#from flask.ext.cors import CORS
logger = logging.getLogger(__name__)


from ams import AmsClient
def start_web(port, web_debug):

    app = Flask(__name__)
    #CORS(app)
    app.debug = web_debug
    app.secret_key = "a123123U36ewbsfbfb"

    client = AmsClient()

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/search")
    def search():

        workGroups = [1,2,3]

        reply = client.search()
        return jsonify(reply)



    logger.info("Starting web on %s", port)
    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()