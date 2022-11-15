from aws_cdk import (

    Stack,
    aws_ec2 as ec2,
    CfnOutput

)
from constructs import Construct

class Ec2InstanceStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        self.instanceName = "ubuntu-server"
        self.instanceType = "t2.micro"
        self.vpc = ec2.Vpc.from_lookup(self, id="VPC", is_default=True)

        sec_group = ec2.SecurityGroup(
            self,
            "sec-group-allow-ssh",
            vpc=self.vpc,
            allow_all_outbound=True,
        )

        # add a new ingress rule to allow port 22 to internal hosts
        sec_group.add_ingress_rule(
            peer=ec2.Peer.ipv4('0.0.0.0/0'),
            description="Allow SSH connection",
            connection=ec2.Port.tcp(22)
        )
        machine_image = ec2.MachineImage.generic_linux(
            {
                'us-west-2': "ami-0a05040be81434d40"
            }
        )
        with open('userdata.sh') as f:
            script = f.read()
        user_data = ec2.UserData.custom(script)

        ec2_instance = ec2.Instance(
            self,
            "ec2-instance",
            instance_name=self.instanceName,
            instance_type=ec2.InstanceType(self.instanceType),
            machine_image=machine_image,
            key_name="bard",
            vpc=self.vpc,
            security_group=sec_group,
            user_data=user_data
        )
        CfnOutput(self, "ip", value=ec2_instance.instance_public_ip)