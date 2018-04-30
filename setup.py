from setuptools import setup, find_packages

setup(
    name='parquetview',
    version='0.1',
    description='Read and edit parquet files from the command line.',
    scripts=['bin/parquetview'],
    install_requires=[
        "boto3==1.4.7",
        "pandas==0.21.0",
        "pyarrow==0.8.0",
        "tabulate==0.8.2"
    ]
)
