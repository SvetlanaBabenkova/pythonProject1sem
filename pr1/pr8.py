def main(x):
    x = x.replace('\n', ' ').replace('\t', '')[1:-1]
    x_parts = x.split(';')
    result = dict()
    for path in x_parts:
        k = path.find('<=')
        if k != -1:
            value = int(path[k + 1: path.find(' %>')])
            key = path[path.find("val \"") + 2: path.rfind("\"")].strip()
            result[key] = value
    return result
