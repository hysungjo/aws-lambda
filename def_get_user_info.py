# 이 함수는 DynamoDB에서 고객정보를 읽어 AmazonConnect에서 사용할 변수로 리턴 한다. 
# 람다 환경설정에서 생성한 DynamoDB에 맞는 환경변수 설정 해줘야 한다.
import json
import boto3
import os

# 환경변수에서 DynamoDB 테이블명 가져오기
dynamodb_tbl = os.environ['tbl_name']

# boto3를 이용해 AWS 리소스 접근 (여기서는 DynamoDB)
dynamo_db = boto3.resource("dynamodb")

# 람다함수 기본코드
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
