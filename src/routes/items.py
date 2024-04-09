from app import app
from flask import request
from requests import get

@app.route("/items/")
def get_items(offset: int = 0, qty: int = 5000):
    """
    remote service:
    - is able to return up to 50000 entries per request
    - response time is 2 seconds per request(no matter of number of items inside)
    - data format: [offset: int, qty: int, data: [{'name': string, 'data': (string data up to 4MB) }, ...]]
    """
    offset = int(request.args.get('offset', 0))
    qty = int(request.args.get('qty', 1))
    data = []
    for j in range(offset, offset+qty):
        resp = get(f'https://jsonplaceholder.example.com/api/data/offset={offset}').json()
        data.append(resp)
    return data
