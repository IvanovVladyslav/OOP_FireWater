import requests

r = requests.get('https://httpbin.org/')
print(r.encoding)

for line in r.iter_lines():
    print(line)