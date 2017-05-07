cjrh_template
=============

This package offers a subclass of ``string.Template``, called ``cjrhTemplate``,
which adds a few extra features to the standard library class.

Get var names in the template
-----------------------------

This method returns a generator of the variable names inside the template:

.. code:: python

   # main.py
   from cjrh_template import cjrhTemplate as Template
   s = '$person1 gave $object to $person2'
   tmpl = Template(s)
   print(set(tmpl.template_vars()))

Output:

.. code:: bash

   $ python main.py
   set('person1', 'object', 'person2')
