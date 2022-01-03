import os

from flask import Flask, jsonify, make_response, request
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier

signature_verifier = SignatureVerifier(os.environ["SLACK_SIGNING_SECRET"])
slack_token = os.environ["SLACK_BOT_TOKEN"]
channel_id = os.environ["SLACK_SEND_CHANNEL_ID"]

client = WebClient(token=slack_token)

app = Flask(__name__)


@app.route("/events", methods=["POST"])
def handle_event():
    if not signature_verifier.is_valid_request(request.get_data(), request.headers):
        return make_response("invalid request", 403)

    payload = request.json
    if payload["type"] == "url_verification":
        return jsonify(challenge=payload["challenge"])

    elif payload["type"] == "event_callback" and payload["event"]["type"] == "message":
        text = payload["event"]["text"]
        response = client.chat_postMessage(channel=channel_id, text=text + "\n----------------------------------------")
        if not response["ok"]:
            return make_response("", 400)
        return make_response("", 200)

    return make_response("", 404)


if __name__ == "__main__":
    app.run()
