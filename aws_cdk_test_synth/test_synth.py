"""The class for managing your AWS CDK code

The class requires the follow mandatory property:
    'filename' (str): the relative path and name of yaml file for compare

See the unit test or documentation for a complete example:
https://github.com/bilardi/aws-cdk-test-synth/tree/master/tests

# license MIT
# support https://github.com/bilardi/aws-cdk-test-synth/issues
"""
import re
import yaml
import unittest
from aws_cdk import core

class TestSynth(unittest.TestCase):
    template = None

    def __init__(self, filename: str, *args, **kwargs):
        """
        initializes the dictionary of Cloudformation properties for comparison
            Args:
                filename (string): relative path and name of yaml file
        """
        self.load_template(filename)
        unittest.TestCase.__init__(self, *args, **kwargs)

    def load_template(self, filename):
        """
        loads the dictionary of Cloudformation properties for comparison
            Args:
                filename (string): relative path and name of yaml file
        """
        try:
            with open(filename) as yaml_file:
                self.template = self.load(yaml_file)
        except Exception as exception:
            if isinstance(exception, IOError):
                pass
            else:
                raise TypeError(exception)

    def synth(self, app):
        """
        synthesizes the CDK app into a cloud assembly
            Args:
                app (construct): CDK app
            Raises:
                NotImplementedError
        """
        raise NotImplementedError        

    def test_synth(self):
        """
        tests the cloud assembly synthesized is the same with that saved
            Returns:
                Nothing if they are the same or the new template synthesized in yaml format
        """
        self.synthesizes('synth')

    # mandatory
    def runTest(self):
        assert(True == True)

    # helpers
    def synthesizes(self, method_name):
        """
        checks the cloud assembly synthesized is the same with that saved
            Args:
                method_name (string): name of method with the stack to assemble
            Returns:
                Nothing if they are the same or the new template synthesized in yaml format
        """
        app = core.App()
        method = getattr(self, method_name)
        method(app)
        template = self.get_template(app, "test")
        if not template == self.template:
            print(self.dict_to_yaml(template))
        self.assertEqual(template, self.template)

    def load(self, filename):
        """
        loads yaml file
            Args:
                filename (string): relative path and name of yaml file
            Return:
                dictionary of Cloudformation properties
        """
        return yaml.full_load(filename)

    def dict_to_yaml(self, template):
        """
        dumps yaml file
            Args:
                template (dict): dictionary of Cloudformation properties
            Return:
                yaml file of Cloudformation properties
        """
        return yaml.dump(template)

    def remove_asset_parameter_identifier(self, string):
        """
        removes the identifier of Asset Parameters
            Args:
                string (string): key or value of property
            Return:
                string without the identifier of Asset Parameters
        """
        pattern = '[0-9a-z]{64,}'
        return re.sub(pattern, '', string)

    def remove_identifier(self, string):
        """
        removes the identifier
            Args:
                string (string): key or value of property
            Return:
                string without the identifier
        """
        pattern = '[0-9A-Z][0-9A-Z][0-9A-Z][0-9A-Z][0-9A-Z][0-9A-Z][0-9A-Z][0-9A-Z]$'
        if re.match(pattern, string[-8:]):
            string = re.sub(pattern, '', string)
        string = self.remove_asset_parameter_identifier(string)
        return string

    def iterator(self, part_of_template):
        """
        iters the properties of the template for removing the identifiers
            Args:
                part_of_template (dict|list|str): value of property
            Return:
                part of template cleaned from the identifiers
        """
        template = {}
        if isinstance(part_of_template, dict):
            for key in part_of_template.keys():
                new_key = self.remove_identifier(key)
                template[new_key] = self.iterator(part_of_template[key])
        if isinstance(part_of_template, list):
            values_list = []
            for value in part_of_template:
                values_list.append(self.iterator(value))
            template = values_list
        if isinstance(part_of_template, str):
            template = self.remove_identifier(part_of_template)
        return template

    def remove_identifiers(self, original_template):
        """
        removes the identifiers
            Args:
                original_template (dict): dictionary of Cloudformation properties
            Return:
                template cleaned from the identifiers
        """
        template = {}
        for key in original_template.keys():
            template[key] = self.iterator(original_template[key])
        return template

    def get_template(self, app, stack_name):
        """
        synthes the template
            Args:
                app (construct): CDK app
                stack_name (string): Name of stack that you want to synth
            Return:
                dictionary of Cloudformation properties
        """        
        template = app.synth().get_stack_by_name(stack_name).template
        return self.remove_identifiers(template)
