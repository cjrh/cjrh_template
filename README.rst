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

There is also a ``allow_repeats`` parameter to ``template_vars()`` that will
allow the generator to return even repeated variable names, depending on the
sequence in which they're found in the template. This could be used to generate
frequency counts of variable names. Default is ``False``.
