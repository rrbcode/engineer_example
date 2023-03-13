import aws_cdk as cdk

from cdk_lambda_function.cdk_lambda_function_stack import CdkLambdaFunctionStack


app = cdk.App()
CdkLambdaFunctionStack(app, "CdkLambdaFunctionStack")

app.synth()
