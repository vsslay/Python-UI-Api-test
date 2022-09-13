import requests

url_to_create_user = "https://demoqa.com/Account/v1/User"
url_to_create_token = "https://demoqa.com/Account/v1/GenerateToken"
url_to_authorize = "https://demoqa.com/Account/v1/Authorized"
url_to_delete_user = "https://demoqa.com/Account/v1/User/"
# url_to_
# url_to_
# url_to_
# url_to_
json = {"userID": "dba2908f-8c1f-4205-ab4f-55745cfea2d3"}
user_data = {
  "userName": "SampleUser",
  "password": "SecretSauce_12345@"
}
b = {
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IlNhbXBsZVVzZXIiLCJwYXNzd29yZCI6IlNlY3JldFNhdWNlXzEyMzQ1QCIsImlhdCI6MTY1NDY3ODk5OX0.GZeOPqbvoUdRGrq27FGViTLsdZn6TWSxXuF0VYbGR2M",
  "expires": "2022-06-15T09:03:19.362Z",
  "status": "Success",
  "result": "User authorized successfully."
}
# print(requests.post(url_to_create_user, user_data))
# print(requests.post(url_to_create_token, user_data))
# print(requests.post(url_to_authorize, user_data))



