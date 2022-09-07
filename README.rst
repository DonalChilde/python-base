###########
Python Base
###########


Installation
************

.. installation_begin

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)

.. code-block:: bash

    pip install -U cookiecutter

Generate a Python project

.. code-block:: bash

    cookiecutter https://github.com/donalchilde/python-base.git

    #With a specific output directory
    cookiecutter -o ~/projects/tmp/ https://github.com/donalchilde/python-base.git

    #With a specific output directory and default values from cookiecutter.json
    cookiecutter --no-input -o ~/projects/tmp/ https://github.com/donalchilde/python-base.git

.. installation_end


Derived from: https://github.com/audreyfeldroy/cookiecutter-pypackage/
