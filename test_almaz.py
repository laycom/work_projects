import work


def test_last_liter():
    tested_data = [
        ['Э3', 1, 3, 5, 7, 10, 'ПЭ3', 5, 6, 9, 12],
        ['Э3', 1, 3, 5, 7, 10, 'ПЭ3', 5, 6, 9, 12, 'ТУ', 5, 7, 9, 10, 15],
        ['Э3', 1, 3, 5, 7, 10],
        [],
        ['Э3', 10, 'ПЭ3', 5]
    ]
    expected_result = ['10, 12', '10, 12', '10, 0', '0, 0', '10, 5']
    result = []
    for value in tested_data:
        result.append(work.last_liter(value))

    assert expected_result == result


def test_dict_mod():
    number_of_files = 5
    tested_data = {
        'Блок НБ112': [['ЫК'], ['10, 12'], ['10, 12'], ['10, 0'], ['0, 0'], ['10, 5']],
        'Блок НВ151': [['ЫК'], ['15, 12'], ['0, 12'], ['10, 10'], ['12, 12']],
        'Блок НЕ151': [['ЫК'], ['10, 12']],
        'Блок НЕ152': [['ЫК']]
    }
    expected_result = (['Блок НБ112', 'ЫК', '10, 12', '10, 12', '10, 0', '0, 0', '10, 5',
                        'Блок НВ151', 'ЫК', '15, 12', '0, 12', '10, 10', '12, 12', '0, 0',
                        'Блок НЕ151', 'ЫК', '10, 12', '0, 0', '0, 0', '0, 0', '0, 0',
                        'Блок НЕ152', 'ЫК', '0, 0', '0, 0', '0, 0', '0, 0', '0, 0',
                        ], 4)
    result = work.dict_mod(tested_data, number_of_files=number_of_files)
    print(result)
    assert expected_result == result
