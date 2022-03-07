import unittest
import requests
import json

class apitests(unittest.TestCase):

    def test_a_Getpeople(self):
        print("Test get people with pagination api")

        r = requests.get("http://127.0.0.1:5000/people")
        username = json.loads(r.text)[0]['username']
        
        self.assertEqual(r.status_code, 200)

    def test_b_Getpeople(self):
        print('''Test get people returning 10 profiles per page for a specified page''')

        r = requests.get("http://127.0.0.1:5000/people/7")
        r_data = json.loads(r.text)

        self.assertEqual(len(r_data), 10)
        self.assertEqual(r.status_code, 200)

    def test_c_Searchprofile(self):
        print('''Test get username profile data''')

        r = requests.get("http://127.0.0.1:5000/people")
        username = json.loads(r.text)[0]['username']

        r = requests.get("http://127.0.0.1:5000/search/" + username)
        self.assertEqual(r.status_code, 200)

    def test_d_Deleteprofile(self):
        print('''Test delete api to remove a username's profile''')

        r = requests.get("http://127.0.0.1:5000/people")
        username = json.loads(r.text)[0]['username']

        r = requests.delete("http://127.0.0.1:5000/search/" + username)
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()