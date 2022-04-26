FROM python:3.9.12-slim-bullseye

COPY ./requirements.txt /
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r /requirements.txt

COPY ./vaued_app.py /
COPY ./association_rules_finder.py /
COPY ./classification_decision_tr_model.py /
COPY ./classification_linear_svm_model.py /
COPY ./classification_logistic_reg_model.py /
COPY ./classification_perceptron_model.py /
COPY ./classification_random_forest_model.py /
COPY ./templates /templates
COPY ./static /static
COPY ./models /models
COPY ./datasets /datasets

CMD [ "python", "vaued_app.py" ]
EXPOSE 9091