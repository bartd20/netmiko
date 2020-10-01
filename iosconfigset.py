from netmiko import ConnectHandler
from datetime import datetime

cisco3 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": 'PASSWORD',
    "device_type": 'cisco_ios',
    "fast_cli": True
}

net_connect = ConnectHandler(**cisco3)
print(net_connect.find_prompt())

#cfg = ['ip domain-lookup','ip name-server 1.1.1.1','ip name-server 1.0.0.1']
#tstart = datetime.now()
#output = net_connect.send_config_set(cfg)
output = net_connect.send_config_from_file(config_file='commands.txt')
output += net_connect.send_command('ping google.com')
#tstop = datetime.now()
#tdelta = tstop-tstart
print(output)
#print(tdelta)

net_connect.disconnect()

