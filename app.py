from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get("msg").lower()
    #Split the words
    words = user_text.split()

    # Response logic for the challenge
    # Response logic based on word count and the word "secret"
    if len(words) > 5 and "secret" in words:
        response = "Whoa... you're so clever! But are you really ready for the flag? Well, here it is... ICECTF{f@k3_ch@tb0T_but_d0nt_f@k3_y0urs3lf}"
    # If there are fewer than 5 words but it contains the word "secret"
    elif len(words) < 5 and "secret" in words:
        response = "Ah, I see you're trying to uncover something... but I don't understand what you want to say. Can you explain it more?"
    # If the sentence has more than 5 words but no "secret"
    elif len(words) > 5 and "secret" not in words:
        response = "Hmm... you've got a lot to say, but I don't see secret in there. Keep trying!"
    else:
        response = "HAAHAHAHAAHHA LOL try again... it's not that easy!"

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

