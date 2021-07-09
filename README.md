# st7_wrap

An opinionated wrapper around the Strand7 / Straus7 API.


## Background

Over the years I've used the Strand7 API on a number of projects, and sometimes the first step was building a quick-and-dirty wrapper. By publishing this as a package I won't need to make a similar one next time a project comes along. If you too can make use of it, all the better.

This is very far from feature complete - I wouldn't recommend depending on this for long-lived or production work.

Feedback is most welcome via GitHub issues.

## Installation

 - Ensure you've installed [Strand7 R3](http://www.strand7.com/r3/) and you're running Preview 42.
 - Make sure the official Strand7 API is installed and running (contact [Strand7 Support](https://www.strand7.com/html/aboutsupport.htm) if this is not the case). So you should be able to do this in the Python REPL:

 ```python
 >>> import St7API
 >>> St7API.St7Init()
 0
 ```

- Then you can install it the usual way:
```
pip install st7_wrap
```

## Quickstart

TODO


