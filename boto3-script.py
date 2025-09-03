#!/usr/bin/python3
import boto3
# Create AWS service clients
ec2_client = boto3.client('ec2')
asg_client = boto3.client('autoscaling')
elbv2_client = boto3.client('elbv2')  # for Application/Network Load Balancers
elb_client = boto3.client('elb')      # for Classic Load Balancers


def list_ec2_instances():
    """List all EC2 instances with their IDs and states."""
    print("\n--- EC2 INSTANCES ---")
    response = ec2_client.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"ID: {instance['InstanceId']} | State: {instance['State']['Name']}")


def list_amis():
    """List all AMIs owned by your account."""
    print("\n--- AMIs (Owned by You) ---")
    response = ec2_client.describe_images(Owners=['self'])
    for image in response['Images']:
        print(f"AMI ID: {image['ImageId']} | Name: {image.get('Name', 'N/A')}")


def list_auto_scaling_groups():
    """List all Auto Scaling Groups."""
    print("\n--- AUTO SCALING GROUPS ---")
    response = asg_client.describe_auto_scaling_groups()
    for group in response['AutoScalingGroups']:
        print(f"ASG Name: {group['AutoScalingGroupName']} | Instances: {len(group['Instances'])}")


def list_launch_templates():
    """List all EC2 Launch Templates."""
    print("\n--- LAUNCH TEMPLATES ---")
    response = ec2_client.describe_launch_templates()
    for template in response['LaunchTemplates']:
        print(f"Template Name: {template['LaunchTemplateName']} | ID: {template['LaunchTemplateId']}")


def list_load_balancers():
    """List all Load Balancers (Classic + ALB/NLB)."""
    print("\n--- LOAD BALANCERS ---")

    # ALB / NLB
    response_v2 = elbv2_client.describe_load_balancers()
    for lb in response_v2['LoadBalancers']:
        print(f"Type: {lb['Type']} | Name: {lb['LoadBalancerName']} | DNS: {lb['DNSName']}")

    # Classic ELB
    response_v1 = elb_client.describe_load_balancers()
    for lb in response_v1['LoadBalancerDescriptions']:
        print(f"Type: Classic | Name: {lb['LoadBalancerName']} | DNS: {lb['DNSName']}")


if __name__ == "__main__":
    # Call all the functions one by one
    list_ec2_instances()
    list_amis()
    list_auto_scaling_groups()
    list_launch_templates()
    list_load_balancers()
