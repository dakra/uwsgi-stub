uwsgi-stub
==========

This is a stub file for the
`python uwsgi module <http://uwsgi-docs.readthedocs.org/en/latest/PythonModule.html>`_
with function signatures and docstrings.

Normally if you ``import uwsgi`` in your python application your editor highlights
it as an error and also doesn't autocomplete any ``uwsgi.*`` functions since
the module is only made available if you run your app in ``uwsgi``.

You can install this package if you want autocompletion and docstrings for
the uwsgi module.

Note that ``ImportError`` is still raised when importing the uwsgi stub module
so you can savely install it just for autocompletion and still use your

.. code-block:: python

    try:
        import uwsgi
        # do stuff with uwsgi module here
    except ImportError:
        # do alternative things if not running in uwsgi



Installation
------------

Install from PyPI using ``pip`` or ``easy_install``.

.. code-block:: bash

    $ pip install uwsgi-stub


Usage
-----

Just ``import uwsgi`` in your editor and enjoy uwsgi docstrings and autocompletion.
