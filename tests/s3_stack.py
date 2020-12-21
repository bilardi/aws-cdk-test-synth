"""The class for managing s3 stack

The class requires the follow properties:
    'id' (str): the suffix name of resource created
    'bucket_name' (str): the name of bucket

All properties are mandatory. See the unit tests for an example.

# license MIT
# support https://github.com/bilardi/aws-cdk-test-synth/issues
"""
from aws_cdk import (core, aws_s3 as s3)

class S3(core.Stack):
    def __init__(self, scope: core.Construct, id: str, bucket_name: str, **kwargs) -> None:
        """
        deploys AWS S3 bucket
            Resources:
                AWS::S3::Bucket with your details
        """
        super().__init__(scope, id, **kwargs)

        s3.Bucket(self, id, bucket_name=bucket_name)
