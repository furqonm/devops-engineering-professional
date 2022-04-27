#!/bin/bash
curl https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
sudo yum install -y amazon-ssm-agent.rpm
sudo systemctl stop amazon-ssm-agent
# Ganti activation code, activation id, dan region.
sudo amazon-ssm-agent -register -code "activation-code" -id "activation-id" -region "region"
sudo systemctl start amazon-ssm-agent