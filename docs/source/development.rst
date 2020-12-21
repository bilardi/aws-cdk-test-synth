Development
===========

This package is used only for testing your AWS CDK code, so it is useful for helping you to implement your **TDD**.

If you want to use this package with your AWS CDK code, you can find an example in the `tests <https://github.com/bilardi/aws-cdk-test-synth/tree/master/tests>`_ folder of this repository.

Run tests
#########

.. code-block:: bash

    cd aws-cdk-test-synth/
    pip3 install --upgrade -r requirements.txt
    python3 -m unittest discover -v

Template saved
##############

If the unittest fails, the class prints the yaml files.
So, if you will have implemented more unittests classes, it will be simple to run one unittest at a time:

.. code-block:: bash

    cd aws-cdk-test-synth/
    python3 -m unittest discover -v -p test_s3_stack.py

And if you will want to compare what it is different with the template saved, you can save the new template:

.. code-block:: bash

    cd aws-cdk-test-synth/
    python3 -m unittest discover -v -p test_s3_stack.py > tests/s3.yaml.2

This approach is comfortable for running your program for comparison, like `Meld <https://meldmerge.org/>`_, diff or fc:

.. code-block:: bash

    cd aws-cdk-test-synth/
    diff tests/s3.yaml tests/s3.yaml.2
