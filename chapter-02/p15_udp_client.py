#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

target_host = "127.0.0.1"
target_port = 80

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# https://stackoverflow.com/questions/37191612/issue-with-receiving-response-from-127-0-0-1-with-udp-client-in-python
client.bind((target_host, target_port))

# send data
client.sendto(b"AAABBBCCC",(target_host,target_port))

# receive data
data, addr = client.recvfrom(4096)

print(data, addr)
