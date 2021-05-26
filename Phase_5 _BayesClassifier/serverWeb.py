import io
import sys
import json

from bottle import route, run, template, request
from webBayesClassifierService import WebServiceBayes

@route('/')
def hello():
    return template('index.html')

@route('/', method="POST")
def returnLabel():
    """Handle the form submission"""
    postdata = request.body.read()
    fix_bytes_value = postdata.replace(b"'", b'"')
    comment = json.dumps(fix_bytes_value.decode('utf-8'))
    commForLabel = comment.replace('+',' ').replace("comment="," ")
    labelToReturn = WebServiceBayes(commForLabel)
    return json.dumps(labelToReturn)

run(host='localhost', port=9090, debug=True)