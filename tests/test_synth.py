import unittest
from aws_cdk_test_synth.test_synth import TestSynth

class TestService(unittest.TestCase):
    t = None

    def __init__(self, *args, **kwargs):
        self.t = TestSynth('tests/s3.yaml')
        unittest.TestCase.__init__(self, *args, **kwargs)

    def test_remove_asset_parameter_identifier(self):
        self.assertEqual(self.t.remove_asset_parameter_identifier('testAsdAsd'), 'testAsdAsd')
        self.assertEqual(self.t.remove_asset_parameter_identifier('"9cc8199e0fe93d7f01d1b2b231bb687a12a00de795a274fecb02f7860538e214"'), '""')
        self.assertEqual(self.t.remove_asset_parameter_identifier('AssetParameters9cc8199e0fe93d7f01d1b2b231bb687a12a00de795a274fecb02f7860538e214S3Bucket'), 'AssetPS3Bucket')
        self.assertEqual(self.t.remove_asset_parameter_identifier('AssetParameters9cc8199e0fe93d7f01d1b2b231bb687a12a00de795a274fecb02f7860538e214ArtifactHash:'), 'AssetPArtifactHash:')

    def test_remove_identifier(self):
        self.assertEqual(self.t.remove_identifier('testAsdAsd'), 'testAsdAsd')
        self.assertEqual(self.t.remove_identifier('"9cc8199e0fe93d7f01d1b2b231bb687a12a00de795a274fecb02f7860538e214"'), '""')
        self.assertEqual(self.t.remove_identifier('testAF53AC38'), 'test')
        self.assertEqual(self.t.remove_identifier('testASDASDAB'), 'test')

if __name__ == '__main__':
    unittest.main()
