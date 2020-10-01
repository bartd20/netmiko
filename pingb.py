from netmiko import ConnectHandler

cisco4 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": 'PASSWORD',
    "device_type": 'cisco_ios'
}

net_connect = ConnectHandler(**cisco4)
print(net_connect.find_prompt())

output = net_connect.send_command("ping", expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'address:', strip_prompt=False, strip_command=False)
output += net_connect.send_command("8.8.8.8", expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r'ms', strip_prompt=False, strip_command=False)

print(output)

net_connect.disconnect()

