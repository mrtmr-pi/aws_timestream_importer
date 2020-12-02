import boto3
import argparse

from CrudAndSimpleIngestionExample import CrudAndSimpleIngestionExample
from CsvIngestionExample import CsvIngestionExample
from botocore.config import Config

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--csv_file_path", help="This file will be used for ingesting records")
    args = parser.parse_args()

    session = boto3.Session()
    write_client = session.client('timestream-write',
                                    config=Config(read_timeout=20,
                                                    max_pool_connections=5000,
                                                    retries={'max_attempts': 10}))

    crud_and_simple_ingestion_example = CrudAndSimpleIngestionExample(write_client)
    csv_ingestion_example = CsvIngestionExample(write_client)

    crud_and_simple_ingestion_example.describe_database()
    crud_and_simple_ingestion_example.describe_table()

    if args.csv_file_path is not None:
        csv_ingestion_example.bulk_write_records(args.csv_file_path)