pdir: Selective & Pretty dir() printing 
=======================================
    
    dir() is a very useful utility function in python which returns an alphabetized 
    list of names comprising the attributes of the given object, and of 
    attributes reachable from it.
    However, a lot many times all the __<something>__ names can be bugging.
    Say you are really interested in knowing the useful methods a Python "list" offers.
    And you do not like the unreadable, unfiltered mess resulting from using dir(deque).
    All you were interested in was this:
      ['append',
       'count',
       'extend',
       'index',
       'insert',
       'pop',
       'remove',
       'reverse',
       'sort']

    Then pdir is the library for you.


Quickstart
==========

You can use import the pdir() function from pdir after installing this package,
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

(Some of the elements substituted with ...)
Wasn't the former clean and better?


Notes
=====

    * pdir is essentially a wrapper around the existing *dir* function.
    * I will be trying to add interesting regular expressions support to further filter out pdir results.
    * Anyone who is interested in the code can for it here. [#todo]

