from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)
CORS(app)

@app.route('/api/processFormData', methods=['POST'])
def process_form_data():
    data = request.get_json()
    input_data = data.get('inputField')
    
    # TODO: subprocess to run ml model

    # Return a response (optional)
    response_data = {"result": "Data processed successfully"}
    print(input_data)
    return jsonify(response_data)

app.run(debug=True)