from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/balance', methods=['POST'])
def balance():
    data = request.get_json()
    equation = data.get('equation')
    balanced_equation = equation  # Placeholder for balancing logic
    return jsonify({'balanced_equation': balanced_equation})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
