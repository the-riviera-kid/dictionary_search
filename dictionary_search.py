def find_key(source_dictionary, target_string):
    h = source_dictionary

    if target_string in str(h.keys()):
        return True
    for i in h.values():
        if isinstance(i, dict):

            if target_string in str(i.keys()):
                return True
            for j in i.values():
                if isinstance(j, dict):

                    if target_string in str(j.keys()):
                        return True

    return False
