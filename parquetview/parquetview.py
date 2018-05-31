#!/usr/bin/env python3.6

import boto3
import io
import json
import pandas as pd
from tabulate import tabulate
import argparse

def get_bundle(bucket=None, key=None):
    """
    Deserialize .parq file from s3 and return as pandas dataframe
    """
    s3 = boto3.client('s3')
    s3_object = s3.get_object(
        Bucket=bucket,
        Key=key
    )
    file = s3_object["Body"].read()
    return pd.read_parquet(
        io.BytesIO(file),
        engine='pyarrow'
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create SQS FIFO queues per project')
    parser.add_argument('-s',
            dest='s3_path',
            help='Path to S3 object, e.g. <bucket_name>/<prefix>/<filename>'
        )

    parser.add_argument('-l',
            dest='local_path',
            help='Path to local object from current directory'
        )

    parser.add_argument('-p',
            dest='print_parquet',
            help='Print tabulate version of the given parquet file',
            action='store_true',
            default=False
    )

    parser.add_argument('-c',
            dest='create_csv',
            help='Create CSV version of the given parquet file',
            action='store_true',
            default=False
        )

    parser.add_argument('-i',
            dest='inspect',
            help='After conversion, allow interactive shell with PDB',
            action='store_true',
            default=False
        )


    args = parser.parse_args()

    bucket, key = args.s3_path.split('/', 1)
    print(bucket, key)
    df = get_bundle(bucket=bucket, key=key)
    
    if args.print_parquet:
        print(tabulate(df, headers='keys', tablefmt='psql'))

    if args.create_csv:
        df.to_csv('output.csv')

    if args.inspect:
        import pdb; pdb.set_trace()
