def find_key(source_dictionary, target_string):
    if target_string not in str(source_dictionary):
        return False
    for i in source_dictionary.values():
        if isinstance(i, dict):
            if target_string not in str(i.keys()):
                return False
    return True
