import unittest
import requests

class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/file"
    DIR_URL = "{}/root".format(API_URL)
    FILE_URL = "{}/root/newfile".format(API_URL)

    def test_1_createfile(self):
        r = requests.post(ApiTest.FILE_URL, json={"data":"Creating this new file\n"})
        self.assertEqual(r.status_code,200)

    def test_2_readdir(self):
        r = requests.get(ApiTest.DIR_URL)
        self.assertEqual(r.status_code,200)

    def test_3_readfile(self):
        r = requests.get(ApiTest.FILE_URL)
        self.assertEqual(r.status_code,200)

    def test_4_updatefile(self):
        r = requests.patch(ApiTest.FILE_URL, json={"data":"This new data will be added to the file\n"})
        self.assertEqual(r.status_code,200)
    
    def test_5_readfile(self):
        r = requests.get(ApiTest.FILE_URL)
        self.assertEqual(r.status_code,200)

    def test_6_deletefile(self):
        r = requests.delete(ApiTest.FILE_URL)
        self.assertEqual(r.status_code,200)
        