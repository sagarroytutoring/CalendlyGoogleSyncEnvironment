import aws_cdk as core
import aws_cdk.assertions as assertions
from calendly_google_sync_environment.calendly_google_sync_environment_stack import CalendlyGoogleSyncEnvironmentStack


def test_sqs_queue_created():
    app = core.App()
    stack = CalendlyGoogleSyncEnvironmentStack(app, "calendly-google-sync-environment")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = CalendlyGoogleSyncEnvironmentStack(app, "calendly-google-sync-environment")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
