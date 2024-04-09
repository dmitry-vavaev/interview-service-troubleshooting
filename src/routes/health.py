from app import app
from flask import Response

@app.route("/health")
def get_health():
    return Response(status=204)

