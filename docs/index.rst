The IITP_INTERPOLATION project
==============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   license

This is the student IITP project. Here is implementation of common interpolation techniques. 

Project paper: https://www.overleaf.com/project/675a076aed19c14b501fd5e3

Installation
------------

To install the IITP_INTERPOLATION project,
run this command in your terminal:

.. code-block:: console

   $ git clone https://github.com/kirbu123/iitp_interpolation.git


Usage
-----

IITP_INTREPOLATION Python's usage looks like:

Init commands:

.. code-block:: console

   $ poetry lock

   $ poetry init

Running project formatting:

.. code-block:: console

   $ nox -rs format

Running project testing:

.. code-block:: console

   $ nox -rs tests

Running project documentation build:

.. code-block:: console

   $ nox -rs docs

Running techniques:

.. code-block:: console

   $ poetry run cartesiangrid [OPTIONS]


.. option:: --[IMAGE PATH]

   Path to the chosen image (default: random generated 512x512)

.. code-block:: console

   $ poetry run nearest_neighbour [OPTIONS]


.. option:: --[IMAGE PATH]

   Path to the chosen image (default: random generated 512x512)

.. code-block:: console

   $ poetry run bilinear [OPTIONS]


.. option:: --[IMAGE PATH]

   Path to the chosen image (default: random generated 512x512)

.. code-block:: console

   $ poetry run bicubic [OPTIONS]


.. option:: --[IMAGE PATH]

   Path to the chosen image (default: random generated 512x512)


