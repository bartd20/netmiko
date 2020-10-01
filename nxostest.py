from netmiko import ConnectHandler
#from getpass import getpass

nxos_dev1 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": 'PASSWORD',
#    "password": getpass(),
    "device_type": 'cisco_nxos',
}

nxos_dev2 = {
    "host": 'nxos2.lasthop.io',
    "username": 'pyclass',
    "password": 'PASSWORD',
    "device_type": 'cisco_nxos',
}

router_list = [nxos_dev1, nxos_dev2]

for dev in router_list:
    net_connect = ConnectHandler(**dev)
    print(net_connect.find_prompt())

net_connect.disconnect() 

