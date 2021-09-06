import unittest
import requests

class TestUser(unittest.TestCase):
    def test_get_user(self):
        res=requests.get('https://reqres.in/api/users?page=2')
        code=res.status_code
        assert code==200, "failed"

    def test_specific_user(self):
        pass
    def test_getJson(self):
        res=requests.get('https://reqres.in/api/users?page=2')
        data = res.json()
        #print(res.json())
        pages=data['total_pages']
        assert pages == 2
