from setuptools import setup, find_packages

setup(
    name='parquet-viewer',
    version='0.1',
    description='Read and edit parquet files from the command line.',
    packages=find_packages(),
    scripts=['parquet-viewer/parquet-viewer'],
    install_requires=[
        "boto3==1.4.7",
        "botocore==1.8.0",
        "mock==2.0.0",
        "pandas==0.21.0",
        "pyarrow==0.8.0",
        "tabulate==0.8.2"
    ]
)
