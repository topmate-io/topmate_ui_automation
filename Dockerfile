FROM python:latest

# Install curl
USER root
RUN apt-get update && apt-get install -y curl && apt-get install -y procps

# Install Chromium Drive
RUN apt-get update && apt-get install chromium -y --fix-broken --fix-missing

# Install required libraries
RUN pip install --upgrade pip && \
    pip3 install selenium && \
    pip3 install pytest && \
    pip3 install behave && \
    pip3 install allure-behave && \
    pip3 install allure-python-commons && \
    pip3 install pandas && \
    pip3 install pause && \
    pip3 install PyYAML && \
    pip3 install requests

WORKDIR /topmate_ui_automation

ARG BROWSER
ENV BROWSER=$BROWSER

COPY config config/
COPY features features/
COPY utilities utilities/
COPY behave.ini behave.ini

RUN mkdir reports/

COPY entrypoint_ui_automation.sh entrypoint_ui_automation.sh

# Define EntryPoint:
ENTRYPOINT ["bash","/topmate_ui_automation/entrypoint_ui_automation.sh"]