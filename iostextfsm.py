from netmiko import ConnectHandler
#from getpass import getpass

cisco4 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": 'PASSWORD',
    "device_type": 'cisco_ios',
}

net_connect = ConnectHandler(**cisco4)
#output1 = net_connect.send_command("show version", use_textfsm=True)
output2 = net_connect.send_command("show lldp neighbors", use_textfsm=True)
#print(type(output1))
#print(output1)
#print(type(output2))
#print(output2)
print(output2[0].get('neighbor_interface'))

net_connect.disconnect()

