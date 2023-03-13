from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_iam as iam,
)

from constructs import Construct


class CdkLambdaFunctionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = _lambda.Function(
            scope=self,
            id="LambdaHelloPlaneta",
            runtime=_lambda.Runtime.PYTHON_3_8,
            timeout=Duration.seconds(amount=30),
            handler="lambda_handler.handler",
            code=_lambda.Code.from_asset("cdk_lambda_function/code"),
        )

        bucket = s3.Bucket(
            scope=self,
            id="bucket-mn",
            bucket_name="mercado-bitcoin-bucket"
        )

        fn.add_to_role_policy(statement=iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "s3:PutObject",
                "s3:ListBucket",
                "s3:PutObjectAcl"
            ],
            resources=[bucket.bucket_arn,
                       f"{bucket.bucket_arn}/*"
                       ]

        ))
