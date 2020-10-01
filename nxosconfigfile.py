from netmiko import ConnectHandler
from datetime import datetime

nxos1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": 'PASSWORD',
    "device_type": 'cisco_nxos',
    #"fast_cli": True
}

nxos2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": 'PASSWORD',
    "device_type": 'cisco_nxos',
    #"fast_cli": True
}

routers = [nxos1, nxos2]

for dev in (routers):
    net_connect = ConnectHandler(**dev)
    print(net_connect.find_prompt())
    output = net_connect.send_config_from_file(config_file='nxos_commands.txt')
    output += net_connect.save_config()
    print(output)

net_connect.disconnect()

