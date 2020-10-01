from netmiko import ConnectHandler
import time

cisco4 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": 'PASSWORD',
    "secret": 'PASSWORD',
    "device_type": 'cisco_ios',
    "session_log": 'ios_session_log.txt'
}

net_connect = ConnectHandler(**cisco4)
print(">find prompt")
print(net_connect.find_prompt())

print(">config mode -> find prompt")
net_connect.config_mode()
print(net_connect.find_prompt())

print(">exit config mode -> find prompt")
net_connect.exit_config_mode()
print(net_connect.find_prompt())

print(">write channel disable")
net_connect.write_channel("disable\n")
print(">2 sec of sleep")
time.sleep(2)
print(">read channel")
output = net_connect.read_channel()
print(output)

print(">enable")
net_connect.enable()
print(net_connect.find_prompt())

net_connect.disconnect()

