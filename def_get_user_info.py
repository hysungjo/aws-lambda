# 이 함수는 DynamoDB에서 고객정보를 읽어 AmazonConnect에서 사용할 변수로 리턴 한다. 
# 람다 환경설정에서 생성한 DynamoDB에 맞는 환경변수 설정 해줘야 한다.
import json
import boto3
import os

# 환경변수에서 DynamoDB 테이블명 가져오기
tbl_name = os.environ['tbl_name']

# boto3를 이용해 AWS 리소스 접근 (여기서는 DynamoDB)
dynamo_db = boto3.resource("dynamodb")

# 람다함수 기본코드
def lambda_handler(event, context):
    # AmazonConnect를 통해 JSON 형식으로 전화번호 전달 (E.164)
    tel = event['Details']['ContactData']['CustomerEndpoint']['Address']
    
    # 환경변수의 테이블명 지정
    tbl = dynamo_db.Table(tbl_name)
    # DynamoDB테이블에서 tel 속성과 매핑하여 아이템을 찾음
    data = tbl.get_item(Key={"tel": tel})
    # 응답결과는 'Item' 키에 실려오고, 상태코드는 'ResponseMetadata'키에 실려옴 
    # 데이터에 'Item' 키가 있다면, 성공 처리하고, AmazonConnect로 데이터를 리턴한다.
    if 'Item' in data:
        http_status_code = data['ResponseMetadata']['HTTPStatusCode']
        message = 'success'
        tel = data['Item']['tel']
        birth = data['Item']['birth']
        status = data['Item']['status']
        name = data['Item']['name']
        title = data['Item']['title']
        level = data['Item']['level']
        position = data['Item']['position']
        ktis_number = data['Item']['ktis_number']
        kt_number = data['Item']['kt_number']
        ktis_email = data['Item']['ktis_email']
        kt_email = data['Item']['kt_email']
        personal_email = data['Item']['personal_email']
        return {
            "http_status_code": http_status_code,
            "message": message,
            "tel": tel,
            "birth": birth,
            "status": status,
            "name": name,
            "title": title,
            "level": level,
            "position": position,
            "ktis_number": ktis_number,
            "kt_number": kt_number,
            "ktis_email": ktis_email,
            "kt_email": kt_email,
            "personal_email": personal_email
        }
        
    # 데이터에 'Item' 키가 없다면, 실패처리한다.
    # 실패 처리 할 때도 상태코드가 있는지 확인하고
    elif 'ResponseMetadata' in data: 
        http_status_code = data['ResponseMetadata']['HTTPStatusCode']
        message = 'fail'
        return { 
            "http_status_code": http_status_code,
            "message": message
        }
        
    # 상태코드도 없다면 메세지만 보낸다.
    else: 
        message = 'fail'
        return { 
            "message": message
        }