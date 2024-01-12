import boto3

def attach_policy(policy_arn, username):
    iam = boto3.client('iam')

    iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )

attach_policy('arn:aws:iam::955428349758:policy/pyAdminAccess','test_user_py')