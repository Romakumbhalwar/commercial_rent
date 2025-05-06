# app/utils.py
def map_yes_no_to_bool(value):
    if isinstance(value, str):
        if value.lower() == 'yes':
            return True
        elif value.lower() == 'no':
            return False
    return None
