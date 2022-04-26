import logging
import re
from flask import (
    Flask,
    jsonify,
    request, render_template,
)
from flask_cors import cross_origin
from flask_prometheus_metrics import register_metrics
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

import association_rules_finder
import classification_logistic_reg_model as lrm
import classification_linear_svm_model as lsm
# import classification_random_forest_model as rfm
import classification_perceptron_model as pm
import classification_decision_tr_model as dtr

logger = logging.getLogger(__name__)
app = Flask(__name__)
is_authenticated = False


@app.route("/", methods=['GET'])
@cross_origin(headers=['Content-Type'])
def root():
    global is_authenticated
    is_authenticated = False
    return render_template("Home.html")


@app.route("/sign_out", methods=["GET"])
@cross_origin(headers=['Content-Type'])
def sign_out():
    global is_authenticated
    is_authenticated = False
    return render_template("Home.html", status="signed_out")


@app.route("/dev", methods=['GET'])
@cross_origin(headers=['Content-Type'])
def dev():
    return render_template("Dev.html")


@app.route("/version", methods=['GET'])
@cross_origin(headers=['Content-Type'])
def version():
    return jsonify(
        {
            "Server": "ML Recommendations Engine Backend",
            "Version": "1.0.2"
        }
    )


@app.route("/MLService/association", methods=['POST'])
@cross_origin(headers=['Content-Type'])
def mine_association_rule():
    req_data = request.json
    result = []

    movi_list = [int(x) for x in re.sub('"', "", str(
        req_data["MOVI_LIST"]).strip()).split(",")]
    print(movi_list)

    if req_data["ALGO"] == 'FPG':
        result = association_rules_finder.get_rules_fp(movi_list)
    elif req_data["ALGO"] == 'APR':
        result = association_rules_finder.get_rules_ap(movi_list)


if __name__ == "__main__":
    # provide app's version and deploy environment/config name to set a gauge metric
    register_metrics(app, app_version="v0.1.2", app_config="staging")

    # Plug metrics WSGI app to your main app with dispatcher
    dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

    run_simple(hostname="0.0.0.0", port=9091, application=dispatcher, use_debugger=True)
