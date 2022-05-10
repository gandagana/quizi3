import requests
import json
import sqlite3
print('რა გადაიღო Nasa-მ თქვენ დაბადების დღეზე')
r_date = input('შეიყვანეთ თქვენი დაბადების თარიღი(YYYY-MM-DD) : ')
key = "eCZgZv298YJdGYwGnHoJRO9Jz5po5T7Coj1taVcz"
payload = {"api_key": key, 'date': r_date}
r = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
stcode = r.status_code
headers = r.headers
txt = r.text
res = r.json()
j = json.dumps(res, indent=4)
r_name = res['title']
print('სახელი ', r_name)
r_img = requests.get(res['url'])
print(r_img)
img = r_img.content
with open('nasa.jpg', 'wb') as file:
    file.write(img)
#ბაზა errorს მიგდებს :(
# conn = sqlite3.connect('nasa.sqlite3')
# c = conn.cursor()
# c.execute("CREATE TABLE IF NOT EXISTS NASA(id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT, date TEXT)")
# c.execute("INSERT INTO NASA (name, date) VALUES (r_name, r_date)")
# conn.commit()
# conn.close()
