import requests

result = requests.get("https://eat-at-unwsp.draylar.dev/api/menu/?date=2021-10-14")
print(result.json())