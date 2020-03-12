.. Packaging Scientific Python documentation master file, created by
   sphinx-quickstart on Thu Jun 28 12:35:56 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

dataframe_spec Documentation
============================

This was inspired by a discussion_ initiated by Gael Varoquaux about
defining a restricted API/protocol to define how dataframe-like
data structures can be used by down-stream libraries.  In particular
this implements the suggestion_

    The return value of __dataframe_interface__() should be a Python
    dict with values that are each convertible to a 1D array, all of
    which must have the same length.

with some slight modifications.  Inspired by `Promise/A+ <https://promisesaplus.com/>`_  this is the start compliance test suite.

.. _discussion: https://discuss.ossdata.org/t/a-dataframe-protocol-for-the-pydata-ecosystem/267
.. _suggestion: https://discuss.ossdata.org/t/a-dataframe-protocol-for-the-pydata-ecosystem/267/3

.. toctree::
   :maxdepth: 2

   installation
   usage
   release-history
   min_versions
