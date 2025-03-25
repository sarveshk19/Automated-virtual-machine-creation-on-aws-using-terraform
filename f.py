from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/save', methods=['POST'])
def save_data():
    data = request.get_json()

    # Save the JSON data to a file
    with open('vm_configuration.json', 'w') as f:
        json.dump(data, f)

    # Execute the Python script
    subprocess.run(['python', 'main`.py'])

    return jsonify({'message': 'Data saved and script executed successfully'})

if __name__ == '__main__':
    app.run(debug=True)
