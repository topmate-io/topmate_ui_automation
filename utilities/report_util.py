import os
from utilities.util_helper import UtilHelper


class ReportUtil():

    @staticmethod
    def upload_report_to_S3():
        """This method upload the allure report to the aws s3 bucket and return the cloud link"""
        print('uploading report to s3')
        report_cloud_url = ''
        filepath = 'test_data/creds.json'
        json_data = UtilHelper.read_JSON(filepath)
        bucket = json_data.get('aws').get('bucket')
        access_key = json_data.get('aws').get('access_key')
        secret_key = json_data.get('aws').get('secret_key')
        current_time = UtilHelper.get_current_time_with_date_IST()

        source_report_folder = os.path.join(os.path.abspath(__file__ + "/../"), "../reports/allure_reports")
        dest_report_folder = f'ui-automation/reports/{current_time}'
        try:
            print(
                f'AWS_ACCESS_KEY_ID={access_key} AWS_SECRET_ACCESS_KEY={secret_key} aws s3 cp --recursive {source_report_folder} s3://{bucket}/{dest_report_folder}')
            os.system(
                f'AWS_ACCESS_KEY_ID={access_key} AWS_SECRET_ACCESS_KEY={secret_key} aws s3 cp --recursive {source_report_folder} s3://{bucket}/{dest_report_folder}')
            report_cloud_url = f"https://{bucket}.s3.amazonaws.com/{dest_report_folder.replace(':', '%3A')}/" + 'index.html'
            print(f'Report successfully uploaded to S3, bucket path: s3://{bucket}/{dest_report_folder}')
        except Exception as e:
            print(f"Exception occurred while uploading allure to S3: {e}")
        return report_cloud_url
