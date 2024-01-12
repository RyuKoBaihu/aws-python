import boto3



def list_managed_policies():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_policies')

    for response in paginator.paginate(Scope="AWS"):
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            Arn = policy['Arn']

            print('AWS managed policies Policy Name: {} Arn'.format(policy_name, Arn))

def list_custom_policies():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_policies')

    for response in paginator.paginate(Scope="Local"):
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            Arn = policy['Arn']

            print('Custom policies Policy Name: {} Arn'.format(policy_name, Arn))

list_custom_policies()
list_managed_policies()
