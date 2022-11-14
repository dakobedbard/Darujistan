import aws_cdk as core
import aws_cdk.assertions as assertions

from darujistan.darujistan_stack import DarujistanStack

# example tests. To run these tests, uncomment this file along with the example
# resource in darujistan/darujistan_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DarujistanStack(app, "darujistan")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
