import requests
import json
from utilities import log_util

log = log_util.get_logs()


def get(host: str, endpoint: str, headers=None, cookies=None) -> json:
    url = host + endpoint
    response = requests.get(url=url, headers=headers, cookies=cookies)
    resp_json = check_response_status_code(url, response)
    return resp_json


def post(host: str, endpoint: str, payload: json, headers=None, cookies=None) -> json:
    url = host + endpoint
    response = requests.post(url=url, json=payload, headers=headers, cookies=cookies)
    resp_json = check_response_status_code(url, response)
    return resp_json


def put(host: str, endpoint: str, payload: json, headers=None, cookies=None) -> json:
    url = host + endpoint
    response = requests.put(url=url, json=payload, headers=headers, cookies=cookies)
    resp_json = check_response_status_code(url, response)
    return resp_json


def delete(host: str, endpoint: str, headers=None, cookies=None) -> json:
    url = host + endpoint
    response = requests.delete(url=url, headers=headers, cookies=cookies)
    resp_json = check_response_status_code(url, response)
    return resp_json


def check_response_status_code(url, response):
    try:
        assert (response.status_code == 200)
        log.info("API CALL SUCCESSFUL for endpoint:" + url)
        log.info("RESPONSE TEXT:" + response.text)
        log.info("RESPONSE HEADERS:" + json.dumps(dict(response.headers)))
    except AssertionError:
        log.info("API CALL FAILED for url:" + url)
        log.info("STATUS CODE:" + str(response.status_code))
        log.info("RESPONSE TEXT:" + response.text)
        log.info("RESPONSE HEADERS:" + json.dumps(dict(response.headers)))
        raise Exception("API CALL FAILED for url:" + url)
    return response.json()
