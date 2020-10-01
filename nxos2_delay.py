from netmiko import ConnectHandler
from datetime import datetime

nxos2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": 'PASSWORD',
    "device_type": 'cisco_nxos',
    "global_delay_factor": 2
}


net_connect = ConnectHandler(**nxos2)
print(net_connect.find_prompt())
tstart = datetime.now()
net_connect.send_command("show lldp neighbors detail")
tstop = datetime.now()
tdelta = tstop-tstart
print("Global delay:")
print(tstart)
print(tstop)
print(tdelta)

tstart = datetime.now()
net_connect.send_command("show lldp neighbors details", delay_factor=8)
tstop = datetime.now()
tdelta = tstop - tstart
print("Command delay:")
print(tstart)
print(tstop)
print(tdelta)

net_connect.disconnect() 

