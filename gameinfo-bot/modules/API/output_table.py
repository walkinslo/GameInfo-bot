def data_to_dict(string):
    lines = string.split('\n')

    data = {}
    key = None
    for line in lines:
        if line.endswith(':'):
            key = line[:-1]
        if line == 'Views':
            pass
        else:
            data[key] = line

    return data