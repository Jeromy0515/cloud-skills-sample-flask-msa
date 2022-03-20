# 2022 클라우드 컴퓨팅 지방기능경기대회 제 1과제 Microservice Architecture 예제 코드
## Language/Framework
#### Python/Flask
#### Service_A Port : 8080
#### Service_B Port : 8081
## How to install package
First, Upload requirements.txt to S3 Bucket

Copy requirements.txt to EC2 instance. using this command
```
aws s3 cp s3://<bucket-name>/requirements.txt ./
```

Install package, using this command
```
pip3 install -r requirements.txt
```

## Modify Source Code
Modify url to Internal ALB DNS name in /vpc-a/app.py
```
url = '<Your-Internal-ALB-DNS-Name>'
```