# coding: utf-8

"""Internal imports"""
from flask import Flask, render_template, request, jsonify
from data_extractor import DataExtractor


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    """Main page"""

    return render_template("index.html")


@app.route('/api', methods=["POST"])
def api():
    """To make a request"""

    if request.method == "POST":
        # Dans request.form["question"], "question" renvoie à la variable question à la ligne 62 en JS dans script.js"

        question = request.form["question"]

        key_words = DataExtractor.get_key_words(question)
        results = DataExtractor.get_gm_data(key_words)
        print(results[0]["address"])
        extract = DataExtractor.get_mw_data(key_words)

        papybot_quote = DataExtractor.get_papybot_quote()
        return jsonify(
            {
                "papybot_response": papybot_quote,
                "address": results[0]["address"],
                "latitude": results[0]["lat"],
                "longitude": results[0]["lng"],
                "extract": extract["extract"]

            })


if __name__ == '__main__':
    app.run(debug=True)
