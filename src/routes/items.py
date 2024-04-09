from app import app
from requests import get

@app.route("/items")
def get_items():
    resp = get('https://jsonplaceholder.typicode.com/comments')

    return resp.json()
