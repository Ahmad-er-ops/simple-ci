from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def calculator():
    return '''
        <form method="POST" action="/result">
            Number 1: <input type="text" name="num1"><br>
            Number 2: <input type="text" name="num2"><br>
            <input type="submit" value="Calculate">
        </form>
    '''

@app.route("/result", methods=["POST"])
def result():
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    total = num1 + num2
    return f"<h2>Result: {total}</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

