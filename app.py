from flask import Flask, jsonify
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app,'/')

@ask.launch
def launch():
    text = execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, 'Hi' )
    return statement(text).simple_card(text)

@ask.intent('TalkWithMeIntent', mapping={'phrase': 'Phrase'})
def response(phrase):
    text = execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, phrase )
    return statement(text).simple_card(text)

#_________________________________________________________________
import tensorflow as tf
import execute

sess = tf.Session()
sess, model, enc_vocab, rev_dec_vocab = execute.init_session(sess, conf='seq2seq_serve.ini')
#_________________________________________________________________

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye")

@ask.session_ended
def session_ended():
    return "", 200

# start app
if (__name__ == "__main__"): 
    app.run(port = 5000) 