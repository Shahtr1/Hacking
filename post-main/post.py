import requests

target_url = "http://10.0.2.9/dvwa/login.php"
data_dict ={"username" : "admin", "password" : "password", "Login" : "submit"}
response = requests.post(target_url, data=data_dict)
print(response.content)