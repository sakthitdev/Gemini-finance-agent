from flask import Flask, jsonify, render_template, request
from agents.gemini_utils import analyze_topic   # updated import

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process_topic", methods=["POST"])
def process_topic():
    topic = request.get_json()["topic"]

    explanation, graph_required, graph_image = analyze_topic(topic)

    return jsonify({
        "explanation": explanation,
        "graph_required": graph_required,
        "graph_base64": graph_image
    })


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    salary = float(data["salary"])
    total = (
        float(data["food"]) + float(data["rent"]) +
        float(data["travel"]) + float(data["bills"]) +
        float(data["other"])
    )

    emi = (data["emi"] == "yes")
    life = (data["life"] == "yes")
    balance = salary - total

    remarks = ""

    if balance < 0:
        remarks += "⚠ Your expenses exceed income.<br>"
    elif balance > 10000:
        remarks += "-- Strong savings this month.<br>"
    else:
        remarks += "ℹ Finances stable.<br>"

    if emi:
        remarks += "-- Closing EMI early is beneficial.<br>"
    if not life:
        remarks += "🛡 Consider life insurance.<br>"

    return jsonify({
        "result": f"""
        <h3>Summary</h3>
        Salary: ₹{salary}<br>
        Expenses: ₹{total}<br>
        Balance: ₹{balance}<br><br>
        <b>Remarks:</b><br>{remarks}
        """
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
