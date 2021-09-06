import requests

res=requests.get('https://reqres.in/api/users?page=2')
code=res.status_code
assert code==200, "failed"

print(res.json())
