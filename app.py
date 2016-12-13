from flask import Flask, jsonify
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app,'/')

@ask.launch
def launch():
    text = execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, 'Hi' )
    return question(text).reprompt("Are you still there?").simple_card(text)

@ask.intent('TalkWithMeIntent', mapping={'phrase': 'Phrase'})
def response(phrase):
    newPhrase = phrase[0].upper() + phrase[1:]
    text = execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, newPhrase )
    if "_UNK" in text:
        text = "Let's talk about something else."
    else:
        text = text.replace(" ' ","'")
    return question(text).reprompt("Are you still there?").simple_card(text)

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