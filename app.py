from __future__ import unicode_literals #backward compatibility for python2

import os, sys

from flask import Flask, request, abort
from router.router import *

from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#Environment variabel
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None) 
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

#Handler
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

#Init API and Webhook
line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

#Router
router(app, parser, line_bot_api)

#Main
if __name__ == "__main__":
    app.run(debug=True, port=os.getenv('PORT', None))