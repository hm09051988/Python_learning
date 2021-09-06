import requests

res=requests.get('https://reqres.in/api/users?page=2')
print(res)

#print(type(res))
#print(dir(res))

#print(res.headers)

code=res.status_code
assert code==201, "failed"
