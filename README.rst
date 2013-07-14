pdir: Selective, Pretty dir printing utlity for Python
======================================================
    
dir() is a very useful utility function in python which returns a list of 
names comprising the attributes of the given object, and of 
attributes reachable from it.
However, a lot many times all those names can be bugging.
Say you are really interested in knowing only the useful methods a Python "list" offers.
And you do not like the unreadable, unfiltered mess resulting from using "dir(list)".

Then pdir should be very useful for you. 
I wrote this bit because something like this is very helpful to me, who quickly needs a 
list of only the important functions a namespace offers; and likes reading clean pretty stuff.


Quickstart
==========

You can use import the *pdir* function from pdir after installing this package,
and consider it as your new dir() friend.

An example:

    >>> from pdir import pdir
    >>> from collections import list
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

    >>> dir(list)
    ['__add__', '__class__', .........................................................
    ..................................................................................
    'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

Some of the elements are substituted with dots (...) here.

**Wasn't the earlier one clean and better?**

pdir > v0.1 also ships with a help utility (alpha)

    >>> pdir(list,help=True)
    -append-
    L.append(object) -- append object to end-

    -count-
    L.count(value) -> integer -- return number of occurrences of value-

    -extend-
    L.extend(iterable) -- extend list by appending elements from the iterable-

**pd** is also available in the new version as an alternative conveneint reference to the **pdir** function.

    >> from pdir import pd
    >> pd(list)

Notes
=====

 * *pdir* is essentially a wrapper around the existing *dir* function.
 * I will be trying to add interesting regular expressions support to further filter out pdir results.
 * Anyone who is interested in the code can see it `here`_.
 * Its at its very rudimentary stage of development and some of its features may be unstable.

.. _here: https://github.com/pramttl/pdir
