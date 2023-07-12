from django.db import models
from django.contrib.auth.models import User as us
from django.contrib.auth.models import AbstractUser
# Create your models here.

class RabInfo(models.Model):
    app_ins_id = models.CharField(max_length=64, default='unverified') # Application instance id
    cell_id = models.CharField(max_length=64, default='unverified') # E-UTRAN Cell id
    ue_ipv4_address = models.CharField(max_length=64, default='unverified') # ue IPv4 addresses
    ue_ipv6_address = models.CharField(max_length=64, default='unverified') # ue IPv6 addresses
    nated_ip_address = models.CharField(max_length=64, default='unverified') # NATed IP addresses
    gtp_teid = models.CharField(max_length=64, default='unverified') # GTP TEID addresses  
    erab_id = models.DecimalField(max_digits=16,decimal_places=0, default= 0) # erab id
    qci = models.DecimalField(max_digits=16,decimal_places=0, default=0 ) # Qos Class indentifier
    erab_mbr_dl = models.DecimalField(max_digits=16,decimal_places=0, default= 0) # Maximun downlink
    erab_mbr_ul = models.DecimalField(max_digits=16,decimal_places=0, default= 0) # Maximun uplink
    erab_gbr_dl = models.DecimalField(max_digits=16,decimal_places=0, default= 0) # Guaranteed downlink
    erab_gbr_ul = models.DecimalField(max_digits=16,decimal_places=0, default= 0) # Guaranteed uplink
    appInstanceId = models.CharField(max_length=64, default='unverified')
    cellId = models.CharField(max_length=64, default='unverified')
    mcc = models.CharField(max_length=64, default='unverified')
    mnc = models.CharField(max_length=64, default='unverified')
    Type = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    value = models.CharField(max_length=64, default='unverified')
    erabId = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    erabGbrDl = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    erabGbrUl = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    erabMbrDl = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    erabMbrUl = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    requestId = models.CharField(max_length=64, default='0')
    def __str__(self):
        return self.app_ins_id

class S1bearerinfo(models.Model):
    temp_ue_id = models.CharField(max_length=64, default='unverified')
    cellId = models.CharField(max_length=64, default='unverified')
    enb_ipAddress = models.CharField(max_length=64, default='unverified')
    enb_tunnelId = models.CharField(max_length=64, default='unverified')
    sGw_ipAddress = models.CharField(max_length=64, default='unverified')
    sGw_tunnelId = models.CharField(max_length=64, default='unverified')
    mmec = models.CharField(max_length=64, default='unverified')
    mtmsi = models.CharField(max_length=64, default='unverified')

class Layer2meas(models.Model):
    app_ins_id = models.CharField(max_length=64, default='unverified')
    cell_id = models.CharField(max_length=64, default='unverified')
    dl_gbr_prb_usage_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    ul_gbr_prb_usage_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    dl_nongbr_prb_usage_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    ul_nongbr_prb_usage_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    dl_total_prb_usage_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    ul_total_prb_usage_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    received_dedicated_preambles_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    received_randomly_selected_preambles_low_range_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    received_randomly_selected_preambles_high_range_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    number_of_active_ue_dl_gbr_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    number_of_active_ue_ul_gbr_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    number_of_active_ue_dl_nongbr_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    number_of_active_ue_ul_nongbr_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    dl_gbr_pdr_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    ul_gbr_pdr_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    dl_nongbr_pdr_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    ul_nongbr_pdr_cell = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    dl_gbr_delay_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    ul_gbr_delay_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    dl_nongbr_delay_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    ul_nongbr_delay_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    dl_gbr_pdr_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    ul_gbr_pdr_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    dl_nongbr_pdr_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    ul_nongbr_pdr_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    dl_gbr_throughput_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    ul_gbr_throughput_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    dl_nongbr_throughput_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    ul_nongbr_throughput_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    dl_gbr_data_volume_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    ul_gbr_data_volume_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    dl_nongbr_data_volume_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )
    ul_nongbr_data_volume_ue = models.DecimalField(max_digits=64,decimal_places=0, default=0 )

class Subscription(models.Model):
    subscription_Id = models.CharField(max_length=64, default='unverified')
    subscription_type = models.CharField(max_length=64, default='unverified')
    