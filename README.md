# st7_wrap

An opinionated wrapper around the Strand7 / Straus7 API.

Over the years I've used the Strand7 API on a number of projects, and sometimes the first step was building a quick-and-dirty wrapper. The appropriate abstraction level was not always the same but I've settled on something like this several times. By publishing it as apackage I won't need to make a simiilar one next time a project comes along. If you too can make use of it, all the better.

This is very far from feature complete - I wouldn't recommend depending on this for long-lived or production work.

Feedback most welcome via GitHub issues.

## Installation

 - Ensure you've installed [Strand7 R3](http://www.strand7.com/r3/) and you're running Preview XXX
 - Make sure the official Strand7 API is installed and running (contact [Strand7 Support](https://www.strand7.com/html/aboutsupport.htm) if this is not the case). So you should be able to do this in the Python REPL:

 ```python
 >>> import St7API
 >>> St7API.St7Init()
 0
 ```

- Then you can install it the usual way
```
pip install st7_wrap
```

## Quickstart

TODO


