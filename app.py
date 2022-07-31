from flask import Flask, render_template, request
import lungCancer

app = Flask(__name__)


@app.route("/")
def function():
    return render_template("index.html")


@app.route("/sub", methods=['POST'])
def submit():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        age = int(request.form["age"])
        smoke = int(request.form["smoke"])
        areq = int(request.form["areq"])
        liquor = int(request.form["liquor"])

        finalPrediction = lungCancer.predictLungCancer(
            [age, smoke, areq, liquor])
        print("final ans", finalPrediction)

        return render_template("prediction.html", pname=fname, plname=lname, finalResult=finalPrediction)


if __name__ == "__main__":
    app.run(debug=True)
