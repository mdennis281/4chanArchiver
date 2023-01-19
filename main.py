from web4chan import Board4chan
from cache4chan import Cache4chan
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/threads')
def getThreads():
    b = Board4chan('b')
    return jsonify(b.getBoardThreads())

@app.route('/thread/replies')
def getReplies():
    b = Board4chan('b')
    id = request.args.get('id')
    return jsonify(b.getThreadReplies(id))

x = Cache4chan('b')
x._threadLoop()
#app.run()

