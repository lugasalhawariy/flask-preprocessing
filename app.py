from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import nltk
nltk.download('punkt')
from nltk import tokenize, word_tokenize

app = Flask(__name__)

df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})

paragraf = ("Pelayanan sempurna, tapi tidak semuanya menyukainya. Menunya juga enak-enak. Aku jadi suka sama ni restoran")
paragraf2 = ("Aku suka kamu. Aku cinta kamu. Aku benci kamu. Aku aku aku dan aku. Wkwkwkwk")

# route
@app.route('/')
def index():
    return render_template('/pages/pandas.html', tables=[df.to_html(classes='data', header="true", index='false')])


@app.route('/split')
def split():
    pisah_kalimat = paragraf.split(".")
    return render_template('/pages/split.html', data=pisah_kalimat, len=len)

@app.route('/nltk_split')
def nltk_split():
    pisah_kalimat = tokenize.sent_tokenize(paragraf2)
    return render_template('/pages/nltk-split.html', data=pisah_kalimat)

@app.route('/nltk_token')
def nltk_token():
    kalimat = ("Sudah jatuh tertimpa tangga")
    pisah_kata = word_tokenize(kalimat)
    return render_template('/pages/nltk-token.html', data=pisah_kata)

@app.route('/stopword')
def stopword():
    stopword = ['yang', 'di', 'ke', 'dari', 'juga', 'dengan']
    kalimat = ("Aku yang dulu bukanlah yang sekarang, dulu ke jogja sendiri sekarang dengan pasangan")
    data = []
    words = kalimat.split()
    for word in words:
        check = word in stopword
        if not check:
            data.append(word)
    return render_template('/pages/stopword.html', data=data) 



@app.route('/json_nltk')
def go_json():
    pisah_kalimat = tokenize.sent_tokenize(paragraf2)
    return jsonify(data=pisah_kalimat)

if __name__ == "__main__":
    app.run(debug=True)