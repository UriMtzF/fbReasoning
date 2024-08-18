from flask import Flask, render_template, jsonify
from model.forward_reasoning import forward_reasoning

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_forward_reasoning', methods=['POST'])
def run_forward():
    # TODO: Make it possible to send a goal and a KB
    goal = 2
    kb = {7: None, 8:None}
    response = forward_reasoning(goal, kb)
    return jsonify({'message': response})


app.run('0.0.0.0', port=8000, debug=True)