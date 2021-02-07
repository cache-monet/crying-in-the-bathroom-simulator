import boto3
from botocore.exceptions import NoCredentialsError

class S3:
  def __init__(self):
    self.s3 = boto3.client('s3')
    self.BUCKET  = 'crying'

  def get_public_url(self, key):
    url = self.s3.generate_presigned_url(
      'get_object',
      Params = {
        'Bucket': self.BUCKET,
        'Key': key
      },
      ExpiresIn = 120,
    )
    return url

  def upload(self, local_file, key):
      try:
          self.s3.upload_file(local_file, self.BUCKET, key)
          print("Upload Successful")
          return True
      except FileNotFoundError:
          print("The file was not found")
          return False
      except NoCredentialsError:
          print("Credentials not available")
          return False
