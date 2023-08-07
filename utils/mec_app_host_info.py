import socket

class MEC_App_Host_Info:
    def __init__(self):
        self.hostname = socket.gethostname() 
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        self.mec_app_ip = s.getsockname()[0]
        s.close()

    def get_hostname(self):
        return self.hostname

    def get_mec_app_ip(self):
        return self.mec_app_ip
