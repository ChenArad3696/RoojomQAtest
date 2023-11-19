from flask import request, jsonify
from app import app
from app.services import process_form_submission


@app.route('/api/submit_form', methods=['POST'])
def submit_form():
    data = request.get_json()

    user_id = data.get('user_id')
    problem_description = data.get('problem_description')
    device_serial_number = data.get('device_serial_number')
    indicator_light1 = data.get('indicator_light1')
    indicator_light2 = data.get('indicator_light2')
    indicator_light3 = data.get('indicator_light3')

    # Process form submission & get the response status
    response_status = process_form_submission(user_id, problem_description, device_serial_number, indicator_light1,
                                              indicator_light2, indicator_light3)

    return jsonify(message='Form submitted successfully', response_status=response_status)
