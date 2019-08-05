import boto3

ec2 = boto3.resource('ec2')


def create_instance():
    aws = ec2.create_instances(
        ImageId='ami-0b61952867ce96c84',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='ec2'
    )
    print('Instance created ' % aws.ImageId)


def display_instances():
    for instance in ec2.instances.all():
        print(
            "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
                instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id,
                instance.state
            )
        )


def terminate_instances():
    for instance in ec2.instances.all():
        instance.terminate()
        print(instance.id % " terminated")
