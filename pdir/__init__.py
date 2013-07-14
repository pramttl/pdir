from pprint import pprint
import urllib

def _withhelp(obj,sanitized_names):
    for attribute in sanitized_names:
        docstr = '%s.%s.__doc__'%(obj.__name__,attribute,)
        docstring_part = str(eval(docstr)).replace('\n','').rstrip()[0:100]
        print  '-' + attribute + '-'
        if docstring_part[-1] == '.' or docstring_part == None:
            print docstring_part 
        else:
            print docstring_part + '-'
        print


def pdir(obj, help=False, spl=False, inner=False):
    '''
    A small wrapper around the dir python function, that lets you do cool things.
        - Pretty printing
        - Filtered dir printing

    - To see a bit of help along with each of the attribute names just pass, help=True
    as an extra parameter

    - Special Methods, Inner methods are disabled by default can be enabled by setting
    spl, inner parameters as True.
    Special methods are those which have 2 leading underscores and 2 trailing ones.
    Inner Methods are those which have one leading underscore.
    '''
    sanitized_names = []
    name_list = dir(obj)

    for name in name_list:
        if name[0:2] == '__' and name[-2:] == '__' and spl == False:
            pass
        elif name[0] == '_' and inner == False:
            pass
        else:
            sanitized_names.append(name)

    if help == False:
        return pprint(sanitized_names)
    else:
        return _withhelp(obj,sanitized_names)


# Alternative convenient name for pdir.
pd = pdir

