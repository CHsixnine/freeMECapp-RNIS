from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import RabInfo,S1bearerinfo,Layer2meas,Subscription
from django.contrib import auth as Auth
from django.utils.datastructures import MultiValueDict
import json,secrets
from django.core import serializers

# Create your views here.

def rab_info(request):
    if request.method == "GET":
        try:
            param = {}
            request_data = request.GET.items()
            for key, value in request_data:
                param[key] = value
            data = RabInfo.objects.get(app_ins_id=param["app_ins_id"])
            result = get_rab_info(data)
            return JsonResponse(result, status=200)
        except Exception as e:
            print(e)
            result = {
                "detail": "incorrect parameters",
                "instance": "None",
                "status": 0,
                "title": "None",
                "type": "None"
            }
            return JsonResponse(result, status=400)

def plmn_info(request):
    if request.method == "GET":
            param = {}
            result = []
            request_data = request.GET.items()
            for key, value in request_data:
                param[key] = value
            for app_ins_id in eval(param["app_ins_id"]):
                if RabInfo.objects.filter(app_ins_id=app_ins_id).first():
                    data = RabInfo.objects.get(app_ins_id=app_ins_id)
                    appInstanceId = data.appInstanceId
                    mcc = data.mcc
                    mnc = data.mnc
                    plmn = []
                    payload = {
                        "mcc": mcc,
                        "mnc": mnc
                    }
                    plmn.append(payload)
                    payload = {
                        "appInstanceId": appInstanceId,
                        "plmn": plmn,
                        "timeStamp": {
                            "nanoSeconds": 0,
                            "seconds": 0
                        }
                    }
                    result.append(payload)
                else:
                    result = {
                        "detail": "incorrect parameters",
                        "instance": "None",
                        "status": 0,
                        "title": "None",
                        "type": "None"
                    }
                    return JsonResponse(result, status=400)
            return HttpResponse([result], status=200)
                
def s1_bearer_info(request):
    if request.method == "GET":
        param = {}
        request_data = request.GET.items()
        for key, value in request_data:
            param[key] = value
            print(param["temp_ue_id"])
        if param["temp_ue_id"] == '':
            result = {
                "detail": "incorrect parameters",
                "instance": "None",
                "status": 0,
                "title": "None",
                "type": "None"
            }
            return JsonResponse(result, status=400)
        else:
            associateId = []
            ecgi = []
            s1BearerInfoDetailed = []
            # print(type(eval(param["temp_ue_id"])))
            for ue_id in eval(param["temp_ue_id"]):
                print(ue_id)
                query = S1bearerinfo.objects.filter(temp_ue_id=ue_id).values()
                for data in query:
                    cellId = data["cellId"]
                    enb_ipAddress = data["enb_ipAddress"]
                    enb_tunnelId = data["enb_tunnelId"]
                    sGw_ipAddress = data["sGw_ipAddress"]
                    sGw_tunnelId = data["sGw_tunnelId"]
                    mmec = data["mmec"]
                    mtmsi = data["mtmsi"]
                    if RabInfo.objects.filter(cell_id=cellId).first():
                        # info = RabInfo.objects.filter(cell_id=cellId).values()
                        info = RabInfo.objects.get(cell_id=cellId)
                    # for index in info:
                        # mcc = index["mcc"]
                        # mnc = index["mnc"]
                        # value = index["value"]
                        payload = {
                            "type": 0,
                            "value": info.value
                            }
                        associateId.append(payload)
                        payload = {
                            "cellId" : cellId,
                            "plmn" : {
                                "mcc": info.mcc,
                                "mnc": info.mnc
                            }
                        }
                        ecgi.append(payload)
                        payload = {
                            "enbInfo": {
                                "ipAddress": enb_ipAddress,
                                "tunnelId": enb_tunnelId
                            },
                            "erabId": 0,
                            "sGwInfo": {
                                "ipAddress": sGw_ipAddress ,
                                "tunnelId": sGw_tunnelId
                            }
                        }
                        s1BearerInfoDetailed.append(payload)

                # print(ue_id)
            s1UeInfo = []
            UeInfo = {
                "associateId": associateId,
                "ecgi": ecgi,
                "s1BearerInfoDetailed": s1BearerInfoDetailed,
                "tempUeId": {
                    "mmec": mmec,
                    "mtmsi": mtmsi
                }
            }
            s1UeInfo.append(UeInfo)
            result = {
                "s1UeInfo": s1UeInfo,
                "timeStamp": {
                    "nanoSeconds": 0,
                    "seconds": 0
                }
            }
            return JsonResponse(result, status=200)
def layer2_meas(request):
    if request.method == "GET":
        param = {}
        request_data = request.GET.items()
        for key, value in request_data:
            param[key] = value
            if param[key] == '':
                result = {
                "detail": "incorrect parameters",
                "instance": "None",
                "status": 0,
                "title": "None",
                "type": "None"
                }
                return JsonResponse(result, status=400)
        print(param["app_ins_id"])
        rab_info_data = RabInfo.objects.filter(app_ins_id=param["app_ins_id"]).values()
        for info in rab_info_data:
            appInstanceId = info["appInstanceId"]
            mcc = info["mcc"]
            mnc = info["mnc"]
            cellId = info["cell_id"]
            value = index["value"]
        cellInfo = {
                "dl_gbr_pdr_cell": 0,
                "dl_gbr_prb_usage_cell": 0,
                "dl_nongbr_pdr_cell": 0,
                "dl_nongbr_prb_usage_cell": 0,
                "dl_total_prb_usage_cell": 0,
                "ecgi": {
                    "cellId": cellId,
                    "plmn": {
                        "mcc": mcc,
                        "mnc": mnc
                    }
                },
                "number_of_active_ue_dl_gbr_cell": 0,
                "number_of_active_ue_dl_nongbr_cell": 0,
                "number_of_active_ue_ul_gbr_cell": 0,
                "number_of_active_ue_ul_nongbr_cell": 0,
                "received_dedicated_preambles_cell": 0,
                "received_randomly_selected_preambles_high_range_cell": 0,
                "received_randomly_selected_preambles_low_range_cell": 0,
                "ul_gbr_pdr_cell": 0,
                "ul_gbr_prb_usage_cell": 0,
                "ul_nongbr_pdr_cell": 0,
                "ul_nongbr_prb_usage_cell": 0,
                "ul_total_prb_usage_cell": 0
            }
        cellUEInfo = {
            "associateId": {
                "type": 0,
                "value": index["value"]
            },
            "dl_gbr_data_volume_ue": 0,
            "dl_gbr_delay_ue": 0,
            "dl_gbr_pdr_ue": 0,
            "dl_gbr_throughput_ue": 0,
            "dl_nongbr_data_volume_ue": 0,
            "dl_nongbr_delay_ue": 0,
            "dl_nongbr_pdr_ue": 0,
            "dl_nongbr_throughput_ue": 0,
            "ecgi": {
                "cellId": cellId,
                "plmn": {
                    "mcc": mcc,
                    "mnc": mnc
                }
            },
            "ul_gbr_data_volume_ue": 0,
            "ul_gbr_delay_ue": 0,
            "ul_gbr_pdr_ue": 0,
            "ul_gbr_throughput_ue": 0,
            "ul_nongbr_data_volume_ue": 0,
            "ul_nongbr_delay_ue": 0,
            "ul_nongbr_pdr_ue": 0,
            "ul_nongbr_throughput_ue": 0
        }

        result = {
            "cellInfo": [cellInfo],
            "cellUEInfo": [cellUEInfo],
            "timeStamp": {
                "nanoSeconds": 0,
                "seconds": 0
            }
        }
        return JsonResponse(result, status=200)

def subscription(request):
    if request.method == "GET":
        param = {}
        request_data = request.GET.items()
        for key, value in request_data:
            param[key] = value
        if param["subscription_type"] == "cell_change":
            subscription_herf = "127.0.0.1:8000"
        elif param["subscription_type"] == "rab_est":
            subscription_herf = "127.0.0.2:8000"
        elif param["subscription_type"] == "rab_mod":
            subscription_herf = "127.0.0.3:8000"
        elif param["subscription_type"] == "rab_rel":
            subscription_herf = "127.0.0.4:8000"
        elif param["subscription_type"] == "meas_rep_ue":
            subscription_herf = "127.0.0.5:8000"
        elif param["subscription_type"] == "nr_meas_rep_ue":
            subscription_herf = "127.0.0.6:8000"
        elif param["subscription_type"] == "timing_advance_ue":
            subscription_herf = "127.0.0.7:8000"
        elif param["subscription_type"] == "ca_reconf":
            subscription_herf = "127.0.0.8:8000"
        elif param["subscription_type"] == "s1_bearer":
            subscription_herf = "127.0.0.9:8000"
        else:
            result = {
                "detail": "incorrect parameters",
                "instance": "None",
                "status": 0,
                "title": "None",
                "type": "None"
                }
            return JsonResponse(result, status=400)
        result = {
            "_links": {
                "self": {
                    "href": subscription_herf
                },
                "subscription": [{
                "href": subscription_herf,
                "subscriptionType": param["subscription_type"]
                }]
            }
        }
        return JsonResponse(result, status=200)
    if request.method == "POST":
        try:
            payload = json.loads(request.body.decode("utf-8"))
            token = secrets.token_hex(16)
            Subscription.objects.create(subscription_Id=token,subscription_type=payload["subscription_type"])
            result = {
                "status" : "Successful subscription",
                "subscription_Id" : token,
                "subscription_type" : payload
            }
            return JsonResponse(result, status=200)
        except:
            result = {
                "detail": "incorrect parameters",
                "instance": "None",
                "status": 0,
                "title": "None",
                "type": "None"
                }
            return JsonResponse(result, status=400)

def subscription_get(request, content):
    if request.method == "GET":        
        if Subscription.objects.filter(subscription_Id=content).first():
            Subscription_data = Subscription.objects.get(subscription_Id=content)
            print(Subscription_data.subscription_type)
            result = {
                "subscriptionId" : content,
                "subscription_type" : Subscription_data.subscription_type,
            }
            return JsonResponse(result, status=200)

    if request.method == "PUT":
        payload = json.loads(request.body.decode("utf-8"))
        Subscription.objects.filter(subscription_Id=content).update(subscription_type=payload["subscription_type"])
        result = "Successfully update subscription"
        return HttpResponse(result, status=200)
    
    if request.method == "DELETE":
        Subscription.objects.filter(subscription_Id=content).delete()
        result = "no content"
        return HttpResponse(result, status=200)

def get_rab_info(data):
    ueInfo = []
    cellUserInfo = []
    erabInfo = []
    associateId = []
    appInstanceId = data.appInstanceId
    cellId = data.cellId
    mcc = data.mcc
    mnc = data.mnc
    value = data.value
    requestId = data.requestId
    payload = {
        "type": 0,
        "value": value
    }
    associateId.append(payload)
    payload = {
        "cellId": cellId,
            "plmn": {
                "mcc": mcc,
                "mnc": mnc
            }
    }
    payload = {
        "erabId": 0,
            "erabQosParameters": {
                "qci": 0,
                "qosInformation": {
                    "erabGbrDl": 0,
                    "erabGbrUl": 0,
                    "erabMbrDl": 0,
                    "erabMbrUl": 0
                }
            }
    }
    erabInfo.append(payload)
    payload = {
        "associateId": associateId,
        "erabInfo": erabInfo
    }
    ueInfo.append(payload)
    payload = {
        "ecgi": {
            "cellId": cellId,
            "plmn": {
                "mcc": mcc,
                "mnc": mnc
            }
        },
        "ueInfo": ueInfo
    }
    cellUserInfo.append(payload)
    result = {
        "appInstanceId": appInstanceId,
        "cellUserInfo": cellUserInfo,
        "requestId": requestId,
        "timeStamp": {
            "nanoSeconds": 0,
            "seconds": 0
        }   
    }
    return result