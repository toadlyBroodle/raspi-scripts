# email-ip.py

Get raspberry pi's network info (gateway/wan ip, local ip, hostname) and email it to oneself. 
This helps locate pi's dynamic IP from remote device, which can then be used to ssh tunnel into pi remotely.
No need to use a third party service such as www.no-ip.com to maintain working dynamic IP address.

To run script on boot, add line `(sleep 30; python3 /PATH/TO/email-ip.py) &` to _/etc/rc.local_.

Create _creds.py_:
```
sender_address = "sender@gmail.com"
sender_password = "password"
sender_server = "smtp.gmail.com"
sender_port = 587
recipient_address = "recipient@domain.com"
```

Inspiration: https://github.com/TheOliver/send-email-with-device-ip-address
