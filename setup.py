from setuptools import setup, find_packages

setup(
    name='parquetview',
    version='0.2',
    description='Read and edit parquet files from the command line.',
    scripts=['parquetview/parquetview'],
    packages=find_packages(),
    install_requires=[
        "boto3==1.4.7",
        "pandas==0.21.0",
        "pyarrow==14.0.1",
        "tabulate==0.8.2"
    ]
)
