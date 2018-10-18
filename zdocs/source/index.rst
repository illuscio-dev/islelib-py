.. islelib documentation master file, created by
   sphinx-quickstart on Mon Oct  1 00:18:03 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

islelib-py
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

islelib is Illuscio's python library template. To build your own documentation, simply
start using it. Below we will show some example documentation with the basic functions
of this library template.

basic useage
------------

   >>> import islelib
   [basic useage example goes here]

Index
-----

* :ref:`setting-up`
* :ref:`writing`
* :ref:`deploying`

Using the islelib Template
==========================

Islelib comes with a number of pre-built quality-of-life macros for developers so they
can code more and manage less, most of which are accessed through make commands.

In addition to your lib's package folder, islelib has two other main directories:

   * ``./zdocs`` - where docs are built to and stored
   * ``./zdevelop`` - where tests, maintenance scripts, and other information is stored

In addition, the following files are used:

   * ``./setup.cfg`` - when possible, settings for all tools are stored here
   * ``./Makefile`` - contains make commands for the suite of tools detailed in this doc

.. _setting-up:

Setting up your Library
=======================

Getting started is easy. Just follow the below steps. Many of these steps include
MakeFile scripts that help you get up and running quickly. To run the make commands,
make sure that the active directory of your terminal session is "islelib-py": ::

   >>> cd /path/to/islelib.py

1. clone islelib-py from gitlab
--------------------------------

2. pick a name
--------------

Illuscio uses the ''isle'' prefix convention (phonetically sounds like I-L/"Aye-EL" as
opposed to "ill". Examples include ``isle_type``, ``isle_collections``, etc.

When you have chosen a name for your new lib, simple type: ::

   >>> make name n=islelib

... where ``islelib`` is the name of your new library. This will:

   * change the name of your main package to ``islelib``
   * change all of the relevant setup.cfg options to ``islelib``
   * change the top level folder to ``islelib-py``
   * remove old ``islelib.egg`` folder
   * redo the install-dev command to generate new ``islelib.egg`` if needed

3. create a virtual environment
--------------------------------

To set up a virtual enviroment through virtualenv, type: ::

   >>> make venv

This will install a new virtual enviroment at ~/venvs/libname-py-[## python version]

example name: ``islelib-py-37``

By default, this command uses your default "python3" alias, but a different version
can be supplied with a `py=` option: ::

   >>> make venv py="/Library/Frameworks/Python.framework/Versions/3.7/bin/python3"
   venv created!
   to enter virtual env, run '. ~/.bash_profile', then 'env_islelib-37'

``make venv`` also registers the enviroment and library directory to your ~/.bash_profile.
This allows you to easily enter a development enviroment in terminal by typing: ::

   >>> env_islelib-37

... where `islelib` is the name of your lib and `37` is the python version of the venv.
This command is equivalent to: ::

   >>> cd /path/to/islelib.py
   >>> source ~/venvs/islelib-py-37/bin/activate

In order to use the new alias, you will need to refresh your current terminal session by
typing: ::

   >>> . ~/.bash_profile

4. install the dev environment
-------------------------------

Islelib already comes pre-built with all the options and tools needed to write a generic
library. To install these tools into a python environment, type: ::

   >>> make install-dev

These tools include automation for building, versioning, testing and docing your new
library.

You will need to have Make installed on your machine. For OSX, you will be prompted
to install make through XCode when you attempt to run this command if it is not
already installed.

.. _writing:

Writing Your Library
====================

1. style
--------

Illuscio's style guide is simple and straightforward:

   1. `Black`_ and `type hints`_ first
   2. `pep8`_ second
   3. When 1 & 2 contradict: see 1

While the writers of this guide may not agree with all opinions of these tools, there is
undeniable benefits to having a consistent, opinionated code style with automated tools.
From `Black's`_ documentation: ::

   By using Black, you agree to cede control over minutiae of hand-formatting. In
   return, Black gives you speed, determinism, and freedom from pycodestyle nagging
   about formatting. You will save time and mental energy for more important matters.

   Black makes code review faster by producing the smallest diffs possible. Blackened
   code looks the same regardless of the project you’re reading. Formatting becomes
   transparent after a while and you can focus on the content instead.

2. lint
-------

To check the formatting of your library, type: ::

   >>> make lint

This will run the following tools to tell you where adjustments need to be made:

   * `flake8`_
   * `Black`_ (checking mode)
   * `MyPy`_

``flake8`` and ``Black`` will both check your formatting and report any instances where
code does not conform to their respective standards. ``Mypy`` is a type checker and
reports instances where typing has been omitted or where type errors are detected,
which can help reduce bugs (ex: passing a known str to a function that only handles
ints.

These lint checks are also performed during deployment, and will cause failed code to
be kept from deploying to production.

3. re-format
------------

Strict pep8 and black adherence, while useful in many ways to the organization, can be
annoying and distracting to individual engineers. To help with this the islelib template
comes with tools to re-format your code for you.

To re-format your code, type: ::

   >>> make format

This will run the following tools:

   * `autopep8`_
   * `Black`_

With these tools, keeping your code properly formatted is minimally invasive, and as an
organization will lead to a more consistent, maintainable codebase.

4. test
-------

Tests are placed in ``zdevelop/tests``, and use the `pytest`_ library. To run your tests
type: ::

   >>> make test

... and watch the magic happen. This macro also creates coverage and error reports.
Coverage reports show what percentage of each file's code is tested. These reports can
be found in the following locations:

   * results: ``zdevelop/tests/_reports/test_results.html``
   * coverage: ``zdevelop/tests/_reports/coverage/index.html``

Illuscio requires >= 85% code coverage in all files to publish a library. Libraries
with less than 85% coverage in any given file will be kicked back or will need to have
an exception granted.

Likewise, code will be tested upon deployment and kicked back in the case of failures.
The brief example tests in this library includes a failed test.

5. document
-----------

islelib uses `Sphinx`_ to create it's documentation. To build docs for your new library,
type: ::

   >>> make doc

Docs will be generated at ``./zdocs/_build/index.html``. This command will also open
the newly created documentation in your default browser. islelib takes advantage of a
few specific sphinx plugins to:

   * automatically annotate types - types DO NOT need to be written in docstring to generate type annotations.
   * style docs with `readthedocs`_ theme

Sphinx offers a number of convenience features for auto-documenting code from
docstrings. Here is a brief example from a function in one of the make scripts:

.. autofunction:: zdevelop.make_scripts.make_name.edit_cfg

.. _deploying:

Deploying Your Library
======================

1. version:
-----------

To version up your library, there are a few options depending on what part of the
``#.#.#`` version number you wish to increment

* 0.1.0 -> 0.1.1 ::

   >>> make version

* 0.1.1 -> 0.2.0 ::

   >>> make version-minor

* 0.2.0 -> 1.0.0 ::

   >>> make version-major

.. web links:
.. _Black: https://black.readthedocs.io/en/stable/
.. _Type Hints: https://mypy.readthedocs.io/en/latest/
.. _Pep8: https://www.python.org/dev/peps/pep-0008/?
.. _Black's: https://black.readthedocs.io/en/stable/
.. _flake8: https://pypi.org/project/flake8/
.. _Mypy: https://mypy.readthedocs.io/en/latest/
.. _autopep8: https://pypi.org/project/autopep8/
.. _pytest: https://docs.pytest.org/en/latest/
.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _readthedocs: https://readthedocs.com/
