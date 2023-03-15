FROM python:latest

# Install curl
USER root
RUN apt-get update && apt-get install -y curl && apt-get install -y procps

# Install Chromium Drive && Allure
RUN apt-get update && apt-get install chromium -y --fix-broken --fix-missing

## Install OpenJDK-8
#RUN apt-get update && \
#    apt-get install -y openjdk-8-jdk && \
#    apt-get install -y ant && \
#    apt-get clean;
#
## Fix certificate issues
#RUN apt-get update && \
#    apt-get install ca-certificates-java && \
#    apt-get clean && \
#    update-ca-certificates -f;

ENV PATH=$PATH:/opt/java/jdk-15.0.2/bin

RUN mkdir /opt/java && \
    curl https://download.java.net/java/GA/jdk15.0.2/0d1cfde4252546c6931946de8db48ee2/7/GPL/openjdk-15.0.2_linux-x64_bin.tar.gz | tar -xz -C /opt/java/

## Setup JAVA_HOME -- useful for docker commandline
#ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
#RUN export JAVA_HOME

RUN apt update && apt install -y npm
RUN npm install -g allure-commandline --save-dev


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
    pip3 install requests && \
    pip3 install awscli

#ENV ALLURE_HOME /usr/local/bin
#RUN export PATH=$ALLURE_HOME:$PATH

WORKDIR /topmate_ui_automation

ARG BROWSER
ENV BROWSER=$BROWSER

COPY config config/
COPY features features/
COPY utilities utilities/
COPY test_data test_data/
COPY behave.ini behave.ini

RUN mkdir reports/

COPY entrypoint_ui_automation.sh entrypoint_ui_automation.sh

# Define EntryPoint:
ENTRYPOINT ["bash","/topmate_ui_automation/entrypoint_ui_automation.sh"]