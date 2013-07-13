from pprint import pprint

def pdir(obj):
    sanitized_names = []
    name_list = dir(obj)
    for name in name_list:
        if name[0:2] == '__' and name[-2:] == '__':
            pass
        else:
            sanitized_names.append(name)
    return pprint(sanitized_names)

