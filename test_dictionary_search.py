def test_find_dictionary():
    dictionary = {'beer': 'pint'}
    string_key = 'beer'
    result = find_key(dictionary, string_key)
    assert result is True
    
