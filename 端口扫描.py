# -*- coding: UTF-8 -*-

import socket

host = 'www.baidu.com'
for i in range(1, 100):
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cli.connect((host, i))
        print("开放端口", i)
    except ConnectionRefusedError as E:
        pass
    cli.close()
