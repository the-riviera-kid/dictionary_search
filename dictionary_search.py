def find_key(source_dictionary, target_string):
    if target_string in str(source_dictionary.keys()):
        return True
    for i in source_dictionary.values():
        if isinstance(i, dict):
            if target_string in str(i.keys()):
                return True
    return False
