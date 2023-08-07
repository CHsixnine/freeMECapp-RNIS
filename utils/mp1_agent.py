from information.settings import MEP_HOST
import requests
import json

class Mp1_Agent():
    def __init__(self):
        pass

    def service_registration(self, appInstanceId, payload):
        self.MEP_SERVICE_REGISTRATION_URL = "http://{MEP_HOST}/mec_service_mgmt/v1/applications/{appInstanceId}/services".format(MEP_HOST=MEP_HOST, appInstanceId=appInstanceId)
        payload = json.dumps(payload)
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cache-Control': 'no-cache',
        }
        response = requests.request("POST", self.MEP_SERVICE_REGISTRATION_URL, headers=headers, data=payload)
        return json.loads(response.text)

    def service_availability_query(self, appInstanceId):
        self.MEP_SERVICE_AVAILABILITY_QUERY_URL = "http://{MEP_HOST}/mec_service_mgmt/v1/applications/{appInstanceId}/services".format(MEP_HOST=MEP_HOST, appInstanceId=appInstanceId)
        payload = ""
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cache-Control': 'no-cache',
        }
        response = requests.request("GET", self.MEP_SERVICE_REGISTRATION_URL, headers=headers, data=payload)
        return json.loads(response.text)

    def access_other_mec_app(self, URL, payload, method, headers):
        pass
