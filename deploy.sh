#!/bin/bash

export AWS_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
cdk synth --parameters --require-approval never
cdk deploy --parameters --require-approval never