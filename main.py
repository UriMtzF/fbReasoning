import copy

from flask import Flask, render_template, jsonify, request
from model.forward_reasoning import forward_reasoning
from model.backward_reasoning import backward_reasoning
from model.rule_set import ruleset
import threading

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

def run_reasonings(goal, kb):
    forward_kb = copy.deepcopy(kb)
    backward_kb = copy.deepcopy(kb)
    forward_result = {}
    backward_result = {}
    forward_solved = False
    backward_solved = False

    def run_forward():
        forward_result['is_solved'], forward_result['message'] = forward_reasoning(goal, forward_kb)

    def run_backward():
        backward_result['is_solved'], backward_result['message'] = backward_reasoning(goal, backward_kb)

    forward_thread = threading.Thread(target=run_forward)
    backward_thread = threading.Thread(target=run_backward)

    forward_thread.start()
    backward_thread.start()

    forward_thread.join()
    backward_thread.join()

    return forward_result, backward_result

@app.route('/run_reasonings', methods=['POST'])
def run_reasonings_route():
    data = request.get_json()
    goal = data['goal']
    kb = {int(k): v for k, v in data['kb'].items()}
    forward_result, backward_result = run_reasonings(goal, kb)
    return jsonify({'forward_message': forward_result['message'], 'backward_message': backward_result['message'], 'forward_solved': forward_result['is_solved'], 'backward_solved': backward_result['is_solved']})

app.run('0.0.0.0', port=8000, debug=True)
