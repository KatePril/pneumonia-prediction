import requests
import json

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
data = {
    'url': 'https://raw.githubusercontent.com/KatePril/test_img/refs/heads/main/502185e27fd4aadd6f1bcc65dd5738d4ed8da4aaec6e901cf5d07fc62768cdf3_big_gallery.jpeg'
}
json_data = json.dumps(data)

res = requests.post(url, data=json_data).json()
print(res)