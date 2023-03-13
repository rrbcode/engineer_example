import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_lambda_function.cdk_lambda_function_stack import CdkLambdaFunctionStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_lambda_function/cdk_lambda_function_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkLambdaFunctionStack(app, "cdk-lambda-function")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
