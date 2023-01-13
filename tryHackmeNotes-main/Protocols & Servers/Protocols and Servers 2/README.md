# Protocols and Servers 2

> Shahrukh Tramboo | February 1st, 2022

--------------------------------------

Consider the ISO/OSI model; we can add encryption to our protocols via the presentation layer. Consequently, data will be presented in an encrypted format (ciphertext) instead of its original form.

Protocol	Default Port	Secured Protocol	Default Port with TLS
---------------------------------------------------------------------
HTTP			80					HTTPS			443
FTP				21					FTPS			990
SMTP			25					SMTPS			465
POP3			110					POP3S			995
IMAP			143					IMAPS			993

---------------------------------------------------------------------

Considering the case of HTTP.

Consequently, HTTPS requires at least the following three steps:

1.	Establish a TCP connection
2.	Establish SSL/TLS connection
3.	Send HTTP requests to the webserver

To establish an SSL/TLS connection, the client needs to perform the proper handshake with the server.

After establishing a TCP connection with the server, the client establishes an SSL/TLS connection with the following steps:

1.	The client sends a ClientHello to the server to indicate its capabilities, such as supported algorithms.
2.	The server responds with a ServerHello, indicating the selected connection parameters. The server provides its certificate if server authentication is required. The certificate is a digital file to identify itself; it is usually digitally signed by a third party. Moreover, it might send additional information necessary to generate the master key, in its ServerKeyExchange message, before sending the ServerHelloDone message to indicate that it is done with the negotiation.
3.	The client responds with a ClientKeyExchange, which contains additional information required to generate the master key. Furthermore, it switches to use encryption and informs the server using the ChangeCipherSpec message.
4.	The server switches to use encryption as well and informs the client in the ChangeCipherSpec message.





