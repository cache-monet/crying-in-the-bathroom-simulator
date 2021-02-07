import json
from music_processor import MusicProcessor
from s3 import S3

def handler(event, context):
  processor = MusicProcessor(outdir='/tmp')
  s3_client = S3()
  local_file, s3_key = processor.process(event.get('yt_url'))
  s3_client.upload(local_file, s3_key)
  public_url = s3_client.get_public_url(s3_key)
  return {
    'statusCode': 200,
    'body': json.dumps({
      'url': public_url
    })
  }
