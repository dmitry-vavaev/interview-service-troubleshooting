from app import app
from flask import request
from requests import get

@app.route("/items/")
def get_items():
    """
    in this api we can get up-to 50000 entries as a response
    remote service data format:
        [offset: 0, data: [{'name': 'name1', 'type': 'type1', }]]
    """
    offset = int(request.args.get('offset', 0))
    qty = int(request.args.get('qty', 0))
    resp = get('https://jsonplaceholder.typicode.com/comments').json()
    data = []
    for j in range(qty):
        data.append(resp[offset+j])
    return data
