import sys, os, time, json
import requests
import mysql.connector as mysql
from random import randint

hero = {
    "id": randint(100, 9999),
    "name": "Batman",
    "identity": "Bruce Wayne",
    "hometown": "Gotham City",
    "age": 40
}

def post_hero(host, data):
    url = 'http://{}/hero'.format(host)
    headers = {'content-type': 'application/json'}
    requests.post(url, data=json.dumps(data), \
        headers=headers)

def get_hero(host, id):
    url = 'http://{}/hero/{}'.format(host, id)
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)    
    return r.json()

def integration_test():
    post_hero(os.environ['WEB_HOST'], hero)
    received_hero = \
        get_hero(os.environ['WEB_HOST'], hero['id'])
    if hero == received_hero:
        print("Integration test passed.")
        time.sleep(2)
    else:
        print("Integration test is not passed.")
        print("The heroes are not the same")
        print("{} != {}".format(hero, received_hero))
        time.sleep(2)
        sys.exit(1)

if __name__ == "__main__":
    integration_test()