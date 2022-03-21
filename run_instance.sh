#!/bin/bash

aws ec2 run-instances \
--image-id ami-xxxxxxxxxxxxxxx \
--count 1 \
--instance-type t2.micro \
--security-group-ids sg-xxxxxxxxxxxxxxx \
--user-data file://user_data.txt \
--subnet-id subnet-xxxxxxxxxxxxxxx \
--tag-specifications "ResourceType=instance, Tags=[{Key=Name,Value=$1}]" \
--iam-instance-profile "Arn=arn:aws:iam::<account-id>:instance-profile/<iam-role-name>"
