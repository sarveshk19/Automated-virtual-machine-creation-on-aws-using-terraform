from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_data():
    # Handle saving data here
    return 'Data saved successfully'

import subprocess

@app.route('/create_instance', methods=['POST'])
def create_instance():
    try: 
        print('Instance creation initiated')
        # Return message before executing Python script
        response_message = 'Instance creation initiated'
        
        # Execute the Python script
        subprocess.run(['python', 'E:\\terraform\\main.py'])
        
        # Return message after script execution
        response_message = 'Instances are created successfully!'
        
        return response_message, 200
    except Exception as e:
        # Return error message if an exception occurs
        return f'Error: {str(e)}', 500


if __name__ == '__main__':
    app.run(debug=True)
