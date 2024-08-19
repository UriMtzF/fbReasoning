from flask import Flask, render_template, jsonify
from model.forward_reasoning import forward_reasoning
from model.backward_reasoning import backward_reasoning
from model.rule_set import ruleset

app = Flask(__name__)


@app.route('/')
def index():
    rules = ""
    for rule in ruleset:
        rule_number = rule[0]
        causes = [f"H{cause}" for cause in rule[1]]
        conclusion = f"H{rule[2]}"
        rules += f"R{rule_number}: {', '.join(causes)} => {conclusion}\n"
    return render_template('index.html', ruleset=rules)


@app.route('/run_forward_reasoning', methods=['POST'])
def run_forward():
    # TODO: Make it possible to send a goal and a KB
    goal = 2
    kb = {7: None, 8: None}
    response = forward_reasoning(goal, kb)
    return jsonify({'message': response})


@app.route('/run_backward_reasoning', methods=['POST'])
def run_backward():
    # TODO: Make it possible to send a goal and a KB
    goal = 2
    kb = {7: None, 8: None}
    response = backward_reasoning(goal, kb)
    return jsonify({'message': response})


app.run('0.0.0.0', port=8000, debug=True)
