.. image:: https://img.shields.io/badge/stdlib--only-yes-green.svg
    :target: https://img.shields.io/badge/stdlib--only-yes-green.svg

.. image:: https://travis-ci.org/cjrh/cjrh_template.svg?branch=master
    :target: https://travis-ci.org/cjrh/cjrh_template

.. image:: https://coveralls.io/repos/github/cjrh/cjrh_template/badge.svg?branch=master
    :target: https://coveralls.io/github/cjrh/cjrh_template?branch=master

.. image:: https://img.shields.io/pypi/pyversions/cjrh_template.svg
    :target: https://pypi.python.org/pypi/cjrh_template

.. image:: https://img.shields.io/github/tag/cjrh/cjrh_template.svg
    :target: https://img.shields.io/github/tag/cjrh/cjrh_template.svg

.. image:: https://img.shields.io/badge/install-pip%20install%20cjrh_template-ff69b4.svg
    :target: https://img.shields.io/badge/install-pip%20install%20cjrh_template-ff69b4.svg

.. image:: https://img.shields.io/pypi/v/cjrh_template.svg
    :target: https://img.shields.io/pypi/v/cjrh_template.svg

.. image:: https://img.shields.io/badge/calver-YYYY.MM.MINOR-22bfda.svg
    :target: http://calver.org/

cjrh_template
=============

This package offers a very thin subclass of ``string.Template``
which adds a few extra features to the standard library class.

**NOTE: this package has no dependencies and will therefore not incur an
additional 3rd-party dependency cost. This is intentional and will not
change.**

Get var names in the template
-----------------------------

The ``placeholders()`` method returns a generator of the variable names
inside the template:

.. code:: python

   # main.py
   from cjrh_template import Template
   s = '$person1 gave $object to $person2'
   tmpl = Template(s)
   print(list(tmpl.placeholders()))

Output:

.. code:: bash

   $ python main.py
   ['person1', 'object', 'person2']

A typical use-case for this is to be able to see a UI with the required
parameters for template substitution. Also, note that the method returns
a generator that will return the names sequentially in a memory-efficient
way.

There is also an ``allow_repeats`` parameter to ``placeholders()`` that will
allow the generator to return even repeated variable names, depending on the
sequence in which they're found in the template. This could be used to generate
frequency counts of variable names. Default is ``False``.
