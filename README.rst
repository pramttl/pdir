pdir: Selective, Pretty dir printing utlity for Python
======================================================
    
dir() is a very useful utility function in python for developers & debuggers,
which returns a list of names comprising the attributes of the given object, 
and of attributes reachable from it. 
However, a lot many times all those names can be bugging.

Case-1: Say you are really interested in knowing only the useful methods a Python "list" offers.
And you do not like the unreadable, unfiltered mess resulting from using "dir(list)".

Case-2: You really love the unix "grep" tool and you want something like that
which allows you to regex filter the results of dir() in a simple call.

Then pdir should be very useful for you. 
I wrote this bit because something like this is very helpful to me, who quickly needs a 
list of only the important functions a namespace offers; likes reading clean pretty stuff;
and really loves the unix "grep" utility.

Your new dir() friends-

* rdir - Regex based dir filtering utility (alternative reference: *rd*)
* pdir - Pretty, convenient dir printing with help (alternative reference: *pd*)


Quickstart
==========

pdir
----

You can use import the *pdir* function from pdir after installing this package,
and consider it as your new dir() friend.

An example:

.. code-block:: python

    >>> from pdir import pdir
    >>> pdir(list)
    ['append',
     'count',
     'extend',
     'index',
     'insert',
     'pop',
     'remove',
     'reverse',
     'sort']

Now lets compare this with what dir(list) prints:

.. code-block:: python

    >>> dir(list)
    ['__add__', '__class__', .........................................................
    ..................................................................................
    'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

Some of the elements are substituted with dots (...) here.

**Wasn't the earlier one clean and better?**

pdir > v0.1 also ships with a help utility (alpha)

.. code-block:: python

    >>> pdir(list,help=True)
    -append-
    L.append(object) -- append object to end- 
    -count-
    L.count(value) -> integer -- return number of occurrences of value-          
    -extend-
    L.extend(iterable) -- extend list by appending elements from the iterable-

**pd** is the alternative reference to the pdir function explained above.

.. code-block:: python

    >>> from pdir import pd
    >>> pd(list)  # Is same as pdir used in the example before.

rdir
----
Having explained pdir, which should probably be the more convenient side of this package,
**rdir** is the more powerful and useful component here.
It allows you to run a regex filter to restrict the names returned by dir.

.. code-block:: python

    >>> from pdir import rdir
    >>> rdir(list,'in')
    ['__contains__', '__init__', 'index', 'insert']
    >>>
    >>> # The above shows a list of items that match the regex='in' filter. Very similar to the unix grep utility.
    >>>
    >>> # To get an inverse list (NOT matching regex) pass the *inv=True* parameter. keyword "inv" is optional.
    >>> rdir(list, '__',True)
    >>> ['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    >>> # ^ returned a list without any '__' (underscores).

The *pdir* function is itself dependent on *rdir* in its internal usage.

rdir -> 
* Does not pretty print by default and returns a list which can be assigned to another object.
* To enable pretty printing, you have to disable return, by providing ret = False as an additional parameter.



Notes
=====

 * *pdir* is essentially a wrapper on *rdir*, which in itself is a wrapper around the Python *dir* function.
 * The code for this tool is available `here`_.
 * Would be glad to see anyone interested in contributing.
 * You can email me or leave an issue on github suggesting improvements.

.. _here: https://github.com/pramttl/pdir
