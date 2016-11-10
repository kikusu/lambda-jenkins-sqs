# coding:utf-8
import boto3


def lambda_handler(event, context):
    """
    :param event:
    :param context:
    """

    del context

    if event["params"]["header"]["X-GitHub-Event"] != 'pull_request':
        return

    if event["body-json"]["action"] not in ["synchronize", "opened"]:
        return

    ec2 = boto3.resource("ec2")

    for instance in ec2.instances.filter(
            Filters=[{'Name': 'tag:Name', 'Values': ['Github-Jenkins']}]):
        print("Start Instance: {}".format(instance.id))
        instance.start()
