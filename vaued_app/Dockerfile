FROM python:3.8-alpine

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir Flask flask_cors flask_prometheus_metrics prometheus-flask-exporter

COPY ./vaued_app.py /
COPY ./association_rules_finder.py /
COPY ./classification_decision_tr_model.py /
COPY ./classification_linear_svm_model.py /
COPY ./classification_logistic_reg_model.py /
COPY ./classification_perceptron_model.py /
COPY ./classification_random_forest_model.py /
COPY ./templates /
COPY ./static /
COPY ./models /
COPY ./datasets /

CMD [ "python", "vaued_app.py" ]
EXPOSE 9091