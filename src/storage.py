# storage.py
import os
import boto3

USE_S3 = False  # flip to True in production

def upload_to_s3(file):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION"),
    )

    key = f"lab_reports/{file.filename}"
    s3.upload_fileobj(file.file, os.getenv("AWS_S3_BUCKET"), key)

    return f"s3://{os.getenv('AWS_S3_BUCKET')}/{key}"

def save_image(file):
    if USE_S3:
        return upload_to_s3(file)  # prod: cloud storage
    return save_image_locally(file)  # dev: local disk
