import requests

users = input("Username ID : ")
password = input("Password ID : ")

headers = {
  "Host": "www.givehub.in.th",
  "content-length": "45",
  "accept": "application/json, text/plain, */*",
  "x-xsrf-token": "eyJpdiI6IkFkZjVGWjBSSmxXK0pKV1IwUU5WTFE9PSIsInZhbHVlIjoiemRsQndxVUpwVzBmVEFkTFwvT1JlNzVuNWo4RXNENEMxanhJRVZobGpqUk0wS3RlY3pZeklXalBqNHZERUhHWFQiLCJtYWMiOiJlMjFiZTk5OTk3MDJkZGNkZDJhOThhMTFjODJmOTIzMzk0MDQ5ZTY2Mzc2NjcxNTEyOTM4MzNjNzEzOGE2MWZjIn0=",
  "sec-ch-ua-mobile": "?0",
  "content-type": "application/json;charset=UTF-8",
  "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
  "sec-ch-ua-platform": "Linux",
  "origin": "https://www.givehub.in.th",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.givehub.in.th/login",
  "cookie": "__gads=ID=138fa42e8e8e2686-223264534ed00089:T=1643603809:RT=1643603809:S=ALNI_MaQxKlolmT34p3XpCq35Z3TSHSDgw;cf_clearance=MNb7isPJonHXe9VQ5cOcEdGlrM9aCyzY5L1DbaW.tfc-1650640082-0-150;XSRF-TOKEN=eyJpdiI6IkFkZjVGWjBSSmxXK0pKV1IwUU5WTFE9PSIsInZhbHVlIjoiemRsQndxVUpwVzBmVEFkTFwvT1JlNzVuNWo4RXNENEMxanhJRVZobGpqUk0wS3RlY3pZeklXalBqNHZERUhHWFQiLCJtYWMiOiJlMjFiZTk5OTk3MDJkZGNkZDJhOThhMTFjODJmOTIzMzk0MDQ5ZTY2Mzc2NjcxNTEyOTM4MzNjNzEzOGE2MWZjIn0%3D;givehubinth_session=eyJpdiI6Inp5U2dPTmlqMldmMUpLK0dZQlwvWXdBPT0iLCJ2YWx1ZSI6IloxWk1SVEkyQnlFU0VVVGU0QnEwcU83Z3lZUkVlTUprcDBGcmJ4UVRoU3pHN2hWd2NmZkFScnlFb2MxcHhLQ1MiLCJtYWMiOiI5YTIwZTRiN2MxNDdkZWEzOWJmZjUzMzU2MTNlZmY0ZDY2MjE1Yjc5ZTk5MGMwMDAzYzViZTA5ODAxOTlmZTJmIn0%3D"
}

json = {
  "username": f"{users}",
  "password": f"{password}"
}

name = requests.post("https://www.givehub.in.th/login",json=json, headers=headers)
print(name.text)