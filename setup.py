import setuptools
import aws_cdk_test_synth

setuptools.setup(
    name="aws-cdk-test-synth",
    version=aws_cdk_test_synth.__version__,
    author=aws_cdk_test_synth.__author__,
    author_email="alessandra.bilardi@gmail.com",
    description="AWS CDK test Synth package",
    long_description=open('README.rst').read(),
    long_description_content_type="text/x-rst",
    url="https://aws-cdk-test-synth.readthedocs.io/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        "Source":"https://github.com/bilardi/aws-cdk-test-synth",
        "Bug Reports":"https://github.com/bilardi/aws-cdk-test-synth/issues",
        "Funding":"https://donate.pypi.org",
    },
)
