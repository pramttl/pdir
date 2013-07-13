pdir: Selective & Pretty dir() printing utlity
==============================================
    
    dir() is a very useful utility function in python which returns a list of 
    names comprising the attributes of the given object, and of 
    attributes reachable from it.
    However, a lot many times all those names can be bugging.
    Say you are really interested in knowing only the useful methods a Python "list" offers.
    And you do not like the unreadable, unfiltered mess resulting from using "dir(list)".

    Then pdir should be very useful for you. 
    I wrote this bit because something like this is very helpful to me, who forgets some of
    the important functions a namespace offers; and likes reading clean pretty stuff.


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

Now lets compare this with what dir() prints:

    >>> dir(list)
    ['__add__', '__class__', .........................................................
    ..................................................................................
    'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

Some of the elements are substituted with dots (...) here.

Wasn't the former clean and better?


Notes
=====

    * pdir is essentially a wrapper around the existing *dir* function.
    * I will be trying to add interesting regular expressions support to further filter out pdir results.
    * Anyone who is interested in the code can see it 'here'_ Its at its very rudimentary stage of development and may be unstable.

.. _here: https://github.com/pramttl/pdir
