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
    requests.post(url, data=json.dumps(data), headers=headers)

def query_db(host, database, user, password, id):
    query = 'SELECT * FROM heroes WHERE id={} limit 1;'.format(id)
    conn = mysql.connect(host=host, user=user, password=password, database=database, auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    cursor.execute(query)     
    (r_id, r_name, r_identity, r_hometown, r_age) = cursor.fetchone()
    cursor.close()
    conn.close()
    return {
        "id": r_id,
        "name": r_name,
        "identity": r_identity,
        "hometown": r_hometown,
        "age": r_age
    }

def integration_test():
    post_hero(os.environ['WEB_HOST'], hero)
    received_hero = query_db(os.environ['DB_HOST'], os.environ['DB_DATABASE'], os.environ['DB_USER'], os.environ['DB_PASSWORD'], hero['id']) 
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