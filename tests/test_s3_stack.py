from tests.s3_stack import S3
from aws_cdk_test_synth.test_synth import TestSynth

class TestS3(TestSynth):

    def __init__(self, *args, **kwargs):
        TestSynth.__init__(self, 'tests/s3.yaml', *args, **kwargs)

    def synth(self, app):
        S3(app, 
            id="test",
            bucket_name="your-bucket-name"
        )
