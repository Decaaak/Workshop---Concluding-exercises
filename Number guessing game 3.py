from flask import Flask, request


app = Flask(__name__)

@app.route("/guess", methods=["GET", "POST"])
def guess_the_number():
    if request.method == "GET":
        return HTML_STR.format(0, 1001)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        answer = request.form.get("answer")
        guess = int(request.form.get("guess", 500))

        if answer == "too big":
            max_number = guess
        elif answer == "too small":
            min_number = guess
        elif answer == "you win":
            return HTML_WINNER.format(guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return HTML.format(guess=guess, min=min_number, max=max_number)










HTML_STR = """
<head>
<title>!!!!! GUESS THE NUMBER !!!!!</title>
</head>
<body>
<h1>Think of a number between 0 and 1000</h1>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}"></input>
    <input type="hidden" name="max" value="{}"></input>
    <input type="submit" value="OK">
</form>
</body>
</html>
"""


HTML = """
<title>!!!!! GUESS THE NUMBER !!!!!</title>
</head>
<body>
<h1>Is it {guess}?</h1>
<form action="" method="POST">
    <input type="submit" name="answer" value="too big">
    <input type="submit" name="answer" value="too small">
    <input type="submit" name="answer" value="you win">
    <!-- <input type="submit" name="answer" value="you won"> -->
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</body>
</html>
"""


HTML_WINNER = """
<head>
<title>!!!!! GUESS THE NUMBER !!!!!</title>
</head>
<body>
<h1>I guessed! Your number is {guess}</h1>
</body>
</html>
"""

if __name__ == '__main__':
    app.run()
