import logging

from flask import (
    Flask, jsonify,
)
from flask_cors import cross_origin
from flask_prometheus_metrics import register_metrics
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/")
@cross_origin(headers=['Content-Type'])
def root():
    return "Welcome to the ML Recommendations Engine Backend"


@app.route("/version")
@cross_origin(headers=['Content-Type'])
def version():
    return jsonify(
        {
            "Server": "ML Recommendations Engine Backend",
            "Version": "1.0.2"
        }
    )


if __name__ == "__main__":
    # provide app's version and deploy environment/config name to set a gauge metric
    register_metrics(app, app_version="v0.1.2", app_config="staging")

    # Plug metrics WSGI app to your main app with dispatcher
    dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

    run_simple(hostname="0.0.0.0", port=9091, application=dispatcher)
