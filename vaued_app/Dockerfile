FROM python:3.8-alpine

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir Flask flask_cors flask_prometheus_metrics prometheus-flask-exporter

COPY ./vaued_app.py /

CMD [ "python", "vaued_app.py" ]
EXPOSE 9091