from pprint import pprint
import urllib

import __builtin__
import inspect, re
from itertools import ifilter, ifilterfalse


def rdir(obj=None, regex='.*', inv=False, ret=True):
    """A wrapper around the dir python function with additional filtering options.
    Selects those names from a dir resposne which match the second regex argument.
     
    Names returned by the builtin function dir() are filtered
    to include only those names matched by the specified regex, or
    not containing the regex incase the inv = True parameter is passed along.

    The function returns a list by default, just pretty prints the filtered names.
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
    A wrapper around the dir python function, that lets you do
        - Pretty printing
        - Gives you quick help showing a sneak into the docstrings for each method
        - Removes special and inner methods in the listing unless specified

    - To see a bit of help along with each of the attribute names just pass, help=True
    as an extra parameter

    - Special Methods, Inner methods are disabled by default can be enabled by setting
    spl, inner parameters as True.
    Special methods are those which have 2 leading underscores and 2 trailing ones.
    Inner Methods are those which have one leading underscore.
    '''
    if spl == False:
        if inner == False:
            sanitized_names = rdir(obj,regex='^_',inv=True)
        else:
            sanitized_names = rdir(obj,regex='^__',inv=True)
    else:
        if inner == False:
            # TODO: Unchecked Case (Though its not very useful)
            # sanitized_names = rdir(obj,regex='^[^_]')
            pass
        else:
            # Then things are as good filtering everything.
            # Smart people should use dir directly for such a case. 
            sanitized_names = __builtin__.dir(obj)
        
    if help == False:
        return pprint(sanitized_names)
    else:
        return _withhelp(obj,sanitized_names)


# Alternative convenient name for pdir.
pd = pdir

