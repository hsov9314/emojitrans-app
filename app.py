# -*- coding: utf-8 -*-

import os
import io
import datetime
from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from flask import send_file
from flask import flash
from translator import get_word_list_janome, wordlist2emoji

app = Flask(__name__)
#app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template("index.html", origin_text="元のテキスト")

    elif request.method == 'POST':
        result = request.form['origin']

        vocab_list = get_word_list_janome(result)
        translated_text = wordlist2emoji(vocab_list)

        return render_template("index.html", origin_text=result, translated_text=translated_text)

if __name__ == '__main__':
    app.run()