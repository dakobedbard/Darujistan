#!/usr/bin/env python3
import os
import aws_cdk as cdk

from darujistan.daru_stack import Ec2InstanceStack

account = os.getenv("AWS_ACCOUNT")
region = "us-west-2"
env = cdk.Environment()
if account and region:
    env = cdk.Environment(account=account, region=region)


app = cdk.App()
Ec2InstanceStack(app, "DaruStack", env=env)

app.synth()
