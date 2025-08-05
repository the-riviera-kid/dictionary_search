def find_key(source_dictionary, target_string):
    h = source_dictionary

    if target_string in str(h.keys()):
        return True
    for i in h.values():
        if isinstance(i, dict):
            result = find_key(i, target_string)
            if result:
                return True

    return False
