FROM python:latest

# Install curl
USER root
RUN apt-get update && apt-get install -y curl && apt-get install -y procps

RUN pip install chromedriver-py

RUN apt-get install -y libglib2.0 libnss3 libgconf-2-4 libfontconfig1

WORKDIR /topmate_ui_automation

ARG BROWSER
ENV BROWSER=$BROWSER

COPY config config/
COPY features features/
COPY utilities utilities/
COPY behave.ini behave.ini
COPY requirements.txt requirements.txt

RUN mkdir reports/

RUN pip install -r requirements.txt

COPY entrypoint_ui_automation.sh entrypoint_ui_automation.sh

# Define EntryPoint:
ENTRYPOINT ["bash","/topmate_ui_automation/entrypoint_ui_automation.sh"]