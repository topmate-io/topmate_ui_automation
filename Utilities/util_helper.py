import json
import os
import random
import string
import uuid
from datetime import datetime
from datetime import timedelta
from zoneinfo import ZoneInfo
import pandas as pd
import pause
import yaml


class UtilHelper:
    selfserve_template_filepath = os.getcwd() + "/testdata/payload/selfserve/"
    allaboard_template_filepath = os.getcwd() + "/testdata/payload/allaboard/"
    env_yaml_filepath = os.getcwd() + "/testdata/envdata/"
    env_testdata_filepath = os.getcwd() + "/testdata/envdata/"

    @staticmethod
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    @staticmethod
    def get_random_string_with_uuid():
        length = UtilHelper.get_random_number(4, 9)
        random_string = 'User_{}_{}'.format(UtilHelper.get_random_string(length), uuid.uuid1())
        return random_string

    @staticmethod
    def get_random_number(start, end):
        number = random.randint(start, end)
        return number

    @staticmethod
    def get_current_time_IST():
        current_time = datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime("%H:%M:%S")
        return current_time

    @staticmethod
    def get_current_time_with_date_IST():
        current_time = datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime("%d.%m.%Y/%H:%M:%S")
        return current_time

    @staticmethod
    def get_current_day_IST():
        current_time = datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime("%A")
        return current_time

    @staticmethod
    def get_rand_username():
        name = ''.join([random.choice(
            string.ascii_letters + string.digits)
            for _ in range(25)])
        return name + "@mt-loadtest.com"

    @staticmethod
    def get_current_time_stamp():
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        return int(timestamp)

    @staticmethod
    def get_current_time_stamp_in_sec():
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        return (timestamp * 1000)

    @staticmethod
    def get_incremented_time_stamp(days, hours, minutes):
        today = datetime.now()
        incremented_time = today + timedelta(days=days) + timedelta(hours=hours) + timedelta(minutes=minutes)
        timestamp = datetime.timestamp(incremented_time)
        return int(timestamp)

    @staticmethod
    def get_decremented_time_stamp(days, hours, minutes):
        today = datetime.now()
        decremented_time = today - timedelta(days=days) - timedelta(hours=hours) - timedelta(minutes=minutes)
        timestamp = datetime.timestamp(decremented_time)
        return int(timestamp)

    @staticmethod
    def pause_until_time(year, month=0, days=0, hours=0, minutes=0, seconds=0):
        dt = datetime(year, month, days, hours, minutes, seconds)
        pause.until(dt)

    @staticmethod
    def convert_days_to_milliseconds(days):
        days = int(days)
        milliseconds = days * 24 * 60 * 60 * 1000
        return milliseconds

    @staticmethod
    def get_base_header():
        base_header = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive'
        }
        return base_header

    @staticmethod
    def get_base_header_with_cookie(cookie):
        cookie_header = UtilHelper.get_base_header()
        cookie_str = ""
        for item in cookie.iteritems():
            cookie_str += item[0] + "=" + item[1]
        cookie_header['Cookie'] = cookie_str
        return cookie_header

    @staticmethod
    def read_JSON(filepath, filename):
        filename = filepath + filename
        with open(filename, 'r') as template:
            data = json.load(template)
        return data

    @staticmethod
    def read_YAML(filepath, filename):
        filename = filepath + filename
        with open(filename, 'r') as template:
            try:
                yaml_data = yaml.safe_load(template)
            except yaml.YAMLError as exc:
                print(exc)
        return yaml_data

    @staticmethod
    def get_value_from_env_yaml(filename, key):
        data_dict = UtilHelper.read_YAML(UtilHelper.env_yaml_filepath, filename)
        return data_dict[key]

    @staticmethod
    def get_percentage(dividend, divisor):
        percentage = (int(dividend) * 100) / int(divisor)
        return percentage

    @staticmethod
    def read_csv(file_path):
        path = os.getcwd() + file_path
        reader = pd.read_csv(path)
        return reader


    @staticmethod
    def read_json(file_path):
        path = os.getcwd() + file_path
        file = open(path)
        return file

    @staticmethod
    def get_column_data_csv(filepath, column_name):
        reader = UtilHelper.read_csv(filepath)
        return reader[column_name]

    @staticmethod
    def get_dict_from_cookieJar(cookies):
        cookie_dict = {}
        for key, value in cookies.items():
            cookie_dict[key] = value
        return cookie_dict

    @staticmethod
    def convert_cookie_to_string(cookies):
        cookie_str = ''
        for key, value in cookies.items():
            cookie_str = cookie_str + '{}={};'.format(key, value)
        return cookie_str

    @staticmethod
    def get_specific_env_var(key):
        env_var = ''
        try:
            env_var = os.environ[key]
            print('Env Var => {} : {}'.format(key, env_var))
        except Exception as e:
            print('!!Failed to get environment data variable for key: {}!!'.format(key))
            print('Exception: {}'.format(e))
            return None
        return env_var
