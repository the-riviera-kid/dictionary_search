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
