#!/usr/bin/python
# -*- conding:utf-8 -*-

import socket

@profile
def blocking_way():
	sock = socket.socket()
	#blocking
	sock.connect(('example.com',80))
	request = 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n'
	sock.send(request.encode('ascii'))
	response = b''
	chunk = sock.recv(4096)
	while chunk:
		response += chunk
		chunk = sock.recv(4096)
	return response


def sync_way():
	res = []
	for i in range(10):
		res.append(blocking_way())
	return len(res)

if __name__ == '__main__':
	sync_way()


