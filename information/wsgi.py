"""
WSGI config for information project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
# from utils.ams_mqtt_client import AMS_MQTT_CLIENT
from utils.mp1_agent import Mp1_Agent
from utils.mec_app_host_info import MEC_App_Host_Info
from information.settings import APPINSTANCE_ID
from django.core.wsgi import get_wsgi_application
import sys



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'information.settings')

application = get_wsgi_application()

mp1 = Mp1_Agent()
mec_app_host_info = MEC_App_Host_Info()

payload = {
  "serInstanceId": mec_app_host_info.get_hostname(),
  "serName": "RNIS",
  "serCategory": {
    "href": mec_app_host_info.get_mec_app_ip()+":"+str(sys.argv[-1].split(':',1)[1]),
    "id": "rnisergtqefhhg",
    "name": "RNI",
    "version": "1.0.0"
  },
  "version": "1.0.0",
  "state": "ACTIVE",
  "transportInfo": {
    "id": "rnisergtqefhhgtransport",
    "name": "rnitsransport",
    "description": "rnis use restapi",
    "type": "REST_HTTP",
    "protocol": "http",
    "version": "2.0",
    "security": {
      "oAuth2Info": {
        "grantTypes": [
          "OAUTH2_AUTHORIZATION_CODE"
        ],
        "tokenEndpoint": "string"
      }
    },
    "implSpecificInfo": {}
  },
  "serializer": "JSON",
  "scopeOfLocality": "MEC-51",
  "consumedLocalOnly": True,
  "isLocal": True,
  "livenessInterval": 0,
  "_links": {
    "self": {
      "href": mec_app_host_info.get_mec_app_ip()+":"+str(sys.argv[-1].split(':',1)[1])
    },
    "liveness": {
      "href": mec_app_host_info.get_mec_app_ip()+":"+str(sys.argv[-1].split(':',1)[1])
    }
  }
}
a = mp1.service_registration(appInstanceId=APPINSTANCE_ID, payload=payload)




