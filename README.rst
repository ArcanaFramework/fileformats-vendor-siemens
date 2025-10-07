How to customise this template
==============================

#. Name your repository with the name fileformats-<SUBPACKAGE-TO-ADD-EXTRAS-TO>
#. Rename the `fileformats/vendor/siemens` directory to the name of the fileformats subpackage the extras are for
#. Search and replace "CHANGEME" with the name of the fileformats subpackage the extras are to be added
#. Replace name + email placeholders in `pyproject.toml` for developers and maintainers
#. Add the extension file-format classes
#. Ensure that all the extension file-format classes are imported into the extras package root, i.e. `fileformats/vendor/siemens`
#. Delete these instructions

...

FileFormats Extension - CHANGEME
====================================
.. image:: https://github.com/arcanaframework/fileformats-vendor-siemens/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/arcanaframework/fileformats-vendor-siemens/actions/workflows/tests.yml
.. image:: https://codecov.io/gh/arcanaframework/fileformats-vendor-siemens/branch/main/graph/badge.svg?token=UIS0OGPST7
    :target: https://codecov.io/gh/arcanaframework/fileformats-vendor-siemens
.. image:: https://img.shields.io/github/stars/ArcanaFramework/fileformats-vendor-siemens.svg
    :alt: GitHub stars
    :target: https://github.com/ArcanaFramework/fileformats-vendor-siemens
.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat
    :target: https://arcanaframework.github.io/fileformats/
    :alt: Documentation Status

This is the "CHANGEME" extension module for the
`fileformats <https://github.com/ArcanaFramework/fileformats-core>`__ package


Quick Installation
------------------

This extension can be installed for Python 3 using *pip*::

    $ pip3 install fileformats-vendor-siemens

This will install the core package and any other dependencies

License
-------

This work is licensed under a
`Creative Commons Attribution 4.0 International License <http://creativecommons.org/licenses/by/4.0/>`_

.. image:: https://i.creativecommons.org/l/by/4.0/88x31.png
  :target: http://creativecommons.org/licenses/by/4.0/
  :alt: Creative Commons Attribution 4.0 International License
