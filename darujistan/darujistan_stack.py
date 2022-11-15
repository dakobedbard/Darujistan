from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam
)
from constructs import Construct


class DarujistanStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc.from_lookup(self, id="VPC", is_default=True)
        with open('userdata.sh') as f:
            script = f.read()
        user_data = ec2.UserData.custom(script)
        print('Creating security group')
        sec_grp = ec2.SecurityGroup(self, 'ec2-sec-grp', vpc=self.vpc, allow_all_outbound=True)
        if not sec_grp:
            print('Failed finding security group')
            return

        print('Creating inbound firewall rule')
        sec_grp.add_ingress_rule(
            peer=ec2.Peer.ipv4('0.0.0.0/24'),
            description='inbound SSH',
            connection=ec2.Port.tcp(22))

        self.role = self._get_role("darujistan-role")

        instance = ec2.Instance(
            self,
            id='darujistan-ec2',
            instance_name='darujistan-ec2',
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3,
                ec2.InstanceSize.SMALL
            ),
            machine_image=ec2.MachineImage.latest_amazon_linux(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            vpc=self.vpc,
            security_group=sec_grp,
            # key_name='bard',
            user_data=user_data
        )


    def _get_role(self, role_name) -> iam.Role:
        policies = {
            'cloud_watch': "arn:aws:iam::aws::policy/CloudWatchLogsFullAccess"
        }
        managed_policies = []
        for policy_type, policy in policies.items():
            if isinstance(policy, str):
                managed_policies.append(
                    iam.ManagedPolicy.from_managed_policy_arn(self, f"darujistan_{policy_type}_policy", policy))
        return iam.Role(
            self,
            "daruistan-role",
            role_name=role_name,
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com')
        )
