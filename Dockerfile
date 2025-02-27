FROM python:latest

# Install curl
USER root
RUN apt-get update && apt-get install -y curl && apt-get install -y procps

# Install Chromium Drive && Allure
RUN apt-get update && apt-get install chromium -y --fix-broken --fix-missing

ENV PATH=$PATH:/opt/java/jdk-15.0.2/bin

# Install Java [allure reporting we must install Java]
RUN mkdir /opt/java && \
    curl https://download.java.net/java/GA/jdk15.0.2/0d1cfde4252546c6931946de8db48ee2/7/GPL/openjdk-15.0.2_linux-x64_bin.tar.gz | tar -xz -C /opt/java/

# install npm to use it to install allure commandline
RUN apt update && apt install -y npm

# install allure-command-line via npm package manager
RUN npm install -g allure-commandline --save-dev

COPY requirements.txt .

# Install required libraries
RUN pip install --upgrade pip && \
    pip3 install -r requirements.txt

WORKDIR /topmate_ui_automation

ARG BROWSER
ENV BROWSER=$BROWSER

ARG URL
ENV URL=$URL

COPY api api/
COPY config config/
COPY features features/
COPY utilities utilities/
COPY test_data test_data/
COPY behave.ini behave.ini

RUN mkdir reports/ && mkdir logs/

COPY entrypoint_ui_automation.sh entrypoint_ui_automation.sh

# Define EntryPoint:
ENTRYPOINT ["bash","/topmate_ui_automation/entrypoint_ui_automation.sh"]