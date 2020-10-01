from netmiko import ConnectHandler
#from getpass import getpass

ios_dev1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": 'PASSWORD',
#    "password": getpass(),
    "device_type": 'cisco_ios',
}

net_connect = ConnectHandler(**ios_dev1)
output = net_connect.send_command("show version")

file = open("iostest_output.txt", mode="w")
file.write(output)
file.close()

net_connect.disconnect()

