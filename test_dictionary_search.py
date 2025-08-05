from dictionary_search import find_key


def test_find_dictionary():
    dictionary = {'beer': 'pint'}
    string_key = 'beer'
    result = find_key(dictionary, string_key)
    assert result is True


def test_empty_dictionary():
    dictionary = {}
    string_key = 'potato'
    result = find_key(dictionary, string_key)
    assert result is False


def test_string_key_not_in_dictionary():
    dictionary = {'beer': 'pint'}
    string_key = 'potato'
    result = find_key(dictionary, string_key)
    assert result is False


def test_dict_in__dict():
    dictionary = {'1': {'beer': 'pint'}}
    string_key = 'beer'
    result = find_key(dictionary, string_key)
    assert result is True


def test_dict_in_inner_dict_value_match():
    dictionary = {'1': {'beer': 'pint'}}
    string_key = 'pint'
    result = find_key(dictionary, string_key)
    assert result is False


def test_dict_in_dict_value_match():
    dictionary = {'1': {'beer': 'pint'}, 'pint': 'of beer'}
    string_key = 'pint'
    result = find_key(dictionary, string_key)
    assert result is True


def test_nested_dict_in_nested_dict_in_dict_value_match():
    dictionary = {'1': {'beer': {'pint': 'of beer'}}}
    string_key = 'pint'
    result = find_key(dictionary, string_key)
    assert result is True


def test_find_key_just_a_whole_bunch_of_dicts():
    dictionary = {
        '1': {
            'beer': {
                'pint': 'of beer'
            },
            'pretty': 'printed',
            'stop': ['hammertime', 'listen'],
            'data': {
                'another': True,
                'dictionary': False,
            },
        },
        '2': {
            'everybody': 'dance now',
            'television': {
                'channel 1': '735hz',
                'channel 23': '823hz',
                'channel 9': {
                    'status': 'OFFLINE',
                    'reason': 'Insulting the queen',
                }
            },
        }
    }
    string_key = 'reason'
    result = find_key(dictionary, string_key)
    assert result is True


