# Getting started with Amazon Timestream with Python

This sample application shows how you can create a database and table, populate the table with ~126K rows of sample data, and run sample queries to jumpstart your evaluation and/or proof-of-concept applications with Amazon Timestream.

----

## Dependencies
- Boto3
- Python3 (Tested with version 3.8.6)

## How to use it

0. (Optional) You can work within a virtual environment
    ```
    python3 -m venv venv
    . venv/bin/activate
    ```

1. Install and configure Boto3 set up following the instructions at https://boto3.amazonaws.com/v1/documentation/api/latest/index.html or executing the following command:
	```sh
	pip3 install -r requirements.txt --upgrade
	```

2. Change `DATABASE_NAME` and `TABLE_NAME` variables in [Constant.py](./Constant.py) file

3. You can copy csv file in to data directory as you wish

3. Run the following commands to insert data into Timestream
    ```sh
    python3 SampleApplication.py --csv_file_path <file_path>
    ```