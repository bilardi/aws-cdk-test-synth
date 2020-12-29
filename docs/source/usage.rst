Usage
=====

The class reads the yaml template saved, synthesizes the new template and compares between them.

You have to import the class **TestSynth** instead of **unittest.TestCase** package and your **TestYourClass** class has to extend it.

.. code-block:: bash

    from tests.test_synth import TestSynth
    from sample.yourclass import YourClass
    class TestYourClass(TestSynth):

The method named **__init__** has to call the class named **TestSynth** with the relative path of yaml template saved.

.. code-block:: bash

    def __init__(self, *args, **kwargs):
        TestSynth.__init__(self, 'tests/yourclass.yaml', *args, **kwargs)

There is the method named **synth** with the initialization of **YourClass**

.. code-block:: bash

    def synth(self, app):
        YourClass(app, id="name-of-your-stack")

If you have to manage more **YourClass**, you can use the method **synthesizes**

.. code-block:: bash

    def your_synth(self, app):
        YourClass(app, id="name-of-your-stack")

    def test_your_synth(self):
        self.synthesizes('your_synth')

It you have to manage more templates, you can use the method **load_template**

.. code-block:: bash

    def your_synth(self, app):
        YourClass(app, id=self.id)

    def test_your_synth(self):
        self.id = "name-of-your-synth"
        self.load_template('tests/yoursynth.yaml')
        self.synthesizes('your_synth')

Example
#######

When you create your **stack.py** file, you can create your **test_stack.py** like the example in the `tests <https://github.com/bilardi/aws-cdk-test-synth/tree/master/tests>`_ folder of this repository.
In that example, you can find

* **s3_stack.py**, the example of your stack implementation
* **test_s3_stack.py**, the example of your unittest class
* **s3.yaml**, the template saved

When you run the unittest (see the `Development <https://aws-cdk-test-synth.readthedocs.io/en/latest/development.html>`_ Section),

* before, you have to create a file empty named **s3.yaml**
* the first time, you have to fill it with the first version
* the times after, if the templates saved and new are different, so the unittest fails, you can evaluate if you have to save a new version or fix your change

You can find other examples in the repositories below:

* `aws-simple-pipeline/tests/test_pipeline_stack.py <https://github.com/bilardi/aws-simple-pipeline/tree/master/tests/test_pipeline_stack.py>`_
* `aws-tool-comparison/cdk/python/tests/ <https://github.com/bilardi/aws-tool-comparison/tree/master/cdk/python/tests/>`_\test_*py
