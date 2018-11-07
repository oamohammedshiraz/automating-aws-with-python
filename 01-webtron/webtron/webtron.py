import boto3
import click

session = boto3.Session(profile_name = 'pythonAuto')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webtron deploys websites to AWS"
    pass

@cli.command('list_buckets')
def list_buckets():
    "list all s3 buckets"
    for bucket in s3.buckets.all():
        print (bucket)
@cli.command('list_bucket_object')
@click.argument('bucket')

def list_bucket_object(bucket):
    "list bucket objects"
    for obj in s3.Bucket(bucket).objects.all():
        print (obj)

if __name__ == '__main__':
    cli();
