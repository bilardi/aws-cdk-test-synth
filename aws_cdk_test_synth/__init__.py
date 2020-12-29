"""AWS CDK test Synth package

This package contains the class for managing your comparison tests
between a yaml template saved and the new template synthesized.

The package works if you use it instead of unittest.TestCase class:
see the documentation on https://aws-cdk-test-synth.readthedocs.io/en/latest/

It is part of the educational repositories (https://github.com/pandle/materials)
to learn how to write stardard code and common uses of the TDD.

Package contents one class. The class reads the yaml template saved,
synthesizes the new template and compares between them.

    >>> import aws_cdk_test_synth
    >>> help(aws_cdk_test_synth)
    >>> import aws_cdk_test_synth.test_synth as TestSynth
    >>> help(TestSynth)

# license MIT
# support https://github.com/bilardi/aws-cdk-test-synth/issues
"""
__version__ = '0.0.2'
__author__ = 'Alessandra Bilardi'
