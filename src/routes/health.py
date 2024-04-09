from app import app
from flask import Response
from routes.items import get_items

@app.route("/health")
def get_health():
    if len(get_items(offset=10, qty=1)) > 0:
        return Response(status=204)
    else:
        return Response(status=500)

