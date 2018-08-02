import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('darksuger.github.io', 80))
s.send(b'GET /index.html HTTP/1.1\r\nHost: darksuger.github.io\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('test.html', 'wb') as f:
    f.write(html)
