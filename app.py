import sys, random
sys.path.insert(0, './src')
import markov
from flask import Flask, render_template

app = Flask(__name__)


markov_chain = markov.main()

@app.route("/")
def home():
    generate_sentence = markov_chain.generate_sentence(25)
    # return render_template("main.html", sentence=generate_sentence)
    return generate_sentence

if __name__ == "__main__":
    app.run(debug=True)