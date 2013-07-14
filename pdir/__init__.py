from pprint import pprint
import urllib

import __builtin__
import inspect, re
from itertools import ifilter, ifilterfalse

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


def pdir(obj=None, help=False, spl=False, inner=False):
    '''
    A wrapper around the dir python function, that lets you do cool things.
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

    if obj:
        name_list = __builtin__.dir(obj)
    else:
        name_list = list(inspect.currentframe().f_back.f_locals.keys())

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


def rdir(obj=None, regex = '.*', inv = False, ret=True):
    """A wrapper around the dir python function with additional filtering options.
    Selects those names from a dir resposne which match the second regex argument.
     
    Names returned by the builtin function dir() are filtered
    to include only those names matched by the specified regex, or
    not containing the regex incase the inv = True parameter is passed along.

    The function does not return by default, just pretty prints the filtered names.
    The result can be returned explicity as a list by setting ret = True.
    """
    if obj:
        name_list = __builtin__.dir(obj)
    else:
        name_list = list(inspect.currentframe().f_back.f_locals.keys())
    if inv == False:
        fil = ifilter
    else:
        fil = ifilterfalse
    if not isinstance(regex, basestring):
        regex = "|".join(regex)

    name_list = list(fil(re.compile(regex).search, name_list))
    if ret == False:
        pprint(name_list)
    else:
        return name_list


# Alternative convenient name for rdir.
rd = rdir

