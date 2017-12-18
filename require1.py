import requests
r=requests.get("http://www.baidu.com")
print(r.raise_for_status())
print(r.status_code)
print(r.headers)
print(r.encoding)
print(r.apparent_encoding)
r.encoding="utf-8"
print(r.text)
