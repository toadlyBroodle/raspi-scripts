#!/usr/bin/python3

import socket
from smtplib import SMTP
import os
import sys
from urllib.request import urlopen

# Import secret informations from file 'secrets.py'
from creds import sender_address
from creds import sender_password
from creds import sender_server
from creds import sender_port
from creds import recipient_address 

def get_network_info():

    try: 
        if os.name == "posix":
            gw = os.popen("ip -4 route show default").read().split()
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((gw[2], 0))
            ipaddr = s.getsockname()[0]
            host = socket.gethostname()
            wan_ip = urlopen('https://api.ipify.org').read().decode('utf8')
            result = ("Gateway:\t" + wan_ip +
		"\nIP:\t\t" + ipaddr +
		"\nHost:\t\t" + host)
            return result
        
        else:
            result = os.name + " not supported yet."
            return result
    except:
        return "Could not detect ip address"

def send_email(network_info):
    try:
        message = ("From: " + sender_address +
		"\nTo: " + recipient_address +
		"\nSubject: Pi ip\n\n" +
		"Raspberry pi booted...\n\n" + network_info)

        server = SMTP(sender_server, sender_port)
        server.ehlo()
        server.starttls()
        server.login(sender_address, sender_password)
        server.sendmail(sender_address, recipient_address, message)
        server.close()
        print("Message sent:\n", message)

    except RuntimeError as e:
        print("failed to send email: " + e.message)

message = get_network_info()
send_email(message)

sys.exit()
