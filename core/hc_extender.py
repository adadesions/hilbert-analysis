import os
import json
from sfcpy import hilbert as hc


def hc_index_generator(order):
    tape = hc.get_hc_tape(order)
    step = (0, 0)
    point_set =[]

    for t in tape:
        _next = hc.tape_reader[t](step)
        step = _next
        point_set.append(step)
    
    return point_set


def hc_write_to_file():
    data = {}
    data['orders'] = {}
    for i in range(2, 10):
        data['orders'][str(i)] = hc_index_generator(i)

    with open('./hc_index.json', 'w') as file:
        json.dump(data, file)
        print('File was written!')


def get_hc_index(order):
    if isinstance(order, int):
        order = str(order)

    dir_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(dir_path, 'hc_index.json')
    with open(json_path, 'r') as index_file:
        data = json.load(index_file)
        return data['orders'][order]


def get_hc_multi_index(max_order=9):
    result = {
        '1': 'odru'
    }

    for i in range(2, max_order+1):
        result[str(i)] = get_hc_index(i)
    
    return result
