# 2022 클라우드 컴퓨팅 지방기능경기대회 제 1과제 Microservice Architecture 예제 코드

## Architecture
![image](https://user-images.githubusercontent.com/77256585/159214736-31253d36-ee59-4817-a6ce-2d4618d9d83b.png)

## Language/Framework
#### Python/Flask
#### Service_A Port : 8080
#### Service_B Port : 8081
#### Health check path : /< v1 or v2 >/health

## Modify Source Code
Modify url to Internal ALB DNS name in [/vpc-a/app.py](https://github.com/Jeromy0515/cloud-skills-msa-example/blob/main/vpc-a/app.py)
```
url = 'http://<Your-Internal-ALB-DNS-Name>'
```

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

## How to Run Application

1. Create internal ALB and modify source code
2. Create EC2 instance for Service-A
   1. Copy [`/vpc-a/app.py`](https://github.com/Jeromy0515/cloud-skills-sample-msa/blob/main/vpc-a/app.py) to EC2 instance
   2. Run `app.py` using this command
      ```
      nohup python3 app.py &
      ```
    
3. Create EC2 instance for Service-B v1
   1. Copy [`/vpc-b/app.py`](https://github.com/Jeromy0515/cloud-skills-sample-msa/blob/main/vpc-b/app.py) to EC2 instance
   2. Run `app.py` using this command
      ```
      nohup python3 app.py &
      ```
4. Create EC2 instance for Service-B v2
   1. Copy [`/vpc-b/test.py`](https://github.com/Jeromy0515/cloud-skills-sample-msa/blob/main/vpc-b/test.py) to EC2 instance
   2. Run `test.py` using this command
      ```
      nohup python3 test.py &
      ```
    

## How to A/B Testing

Configure internal ALB listener rules
```
IF
Path is /v2/*

THEN
Foward to <V2 Target Group>
```

