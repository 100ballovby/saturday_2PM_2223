def get_formatted_name(first, last, middle=''):
    """Build a formatted name and surname"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
