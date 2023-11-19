from app.models import FormSubmission
from app import db

r1 = "please upgrade your device"
r2 = "turn on the device"
r3 = "Please wait"
r4 = "All is ok"
r5 = "Bad serial number"
r6 = "Unknown device"


def process_form_submission(user_id, problem_description, device_serial_number, indicator_light1, indicator_light2,
                            indicator_light3):
    # Asserting serial number type
    if type(device_serial_number) is int:
        device_serial_number = "bad input"
        response_status = r5
    else:
        initial_serial_number = device_serial_number[:4]
        indicator_lights = [indicator_light1, indicator_light2, indicator_light3]
        response_status = serial_number_response(initial_serial_number, indicator_lights)

    save_data_to_DB(user_id, problem_description, device_serial_number, indicator_light1, indicator_light2,
                    indicator_light3, response_status)

    return response_status


def save_data_to_DB(user_id, problem_description, device_serial_number, indicator_light1, indicator_light2,
                    indicator_light3, response_status):
    form_submission = FormSubmission(
        user_id=user_id,
        problem_description=problem_description,
        device_serial_number=device_serial_number,
        indicator_light1=indicator_light1,
        indicator_light2=indicator_light2,
        indicator_light3=indicator_light3,
        response_status=response_status
    )

    # db.drop_all()
    db.create_all()
    db.session.add(form_submission)
    db.session.commit()
    return


def serial_number_response(initial_serial_number, indicator_lights):
    if initial_serial_number == "24-X":
        return r1
    elif initial_serial_number == "36-X":
        return response_36X(indicator_lights)
    elif initial_serial_number == "51-B":
        return response_51B(indicator_lights)
    return r6


def response_36X(indicator_lights):
    if indicator_lights.count("off") == 3:
        return r2
    elif indicator_lights.count("blinking") >= 2:
        return r3
    elif indicator_lights.count("on") == 3:
        return r4
    return


def response_51B(indicator_lights):
    if indicator_lights.count("off") == 3:
        return r2
    elif indicator_lights.count("blinking") >= 1:
        return r3
    # After prior elif no need to check if others are off
    elif indicator_lights.count("on") > 1:
        return r4
    return
