from flask import Flask, request
import random


@app.post("/api/try")
def trial():
    thread = threading.Thread(target=reply(request.form.get("response_url")))
    thread.start()

    return {"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Processing"
      }
    }]}

