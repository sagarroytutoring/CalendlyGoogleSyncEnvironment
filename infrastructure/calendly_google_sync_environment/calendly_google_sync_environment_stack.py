from constructs import Construct
from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_ssm as ssm,
    aws_lambda as lambda_,
    aws_s3 as s3,
    CfnOutput
)
import json


class CalendlyGoogleSyncEnvironmentStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        with open("proton-inputs.json") as f:
            input_file_load = json.load(f)

        # TODO: add error handling
        inputs = input_file_load['environment']['inputs']
        calendly_book_ahead = inputs['calendlySourceEventBookAheadDays']
        calendly_event_id = inputs['calendlySourceEventId']
        calendly_source_bearer_token = inputs['calendlySourceBearerToken']
        google_project_id = inputs['googleCloudProjectId']
        google_target_calendar_id = inputs['googleTargetCalendarId']
        parameter_path = inputs['parameterStorePath']
        google_calendar_config_layer_bucket_name = inputs['googleCalendarConfigLayerS3BucketName']
        google_calendar_config_layer_file_name = inputs['googleCalendlarConfigLayers3Key']

        calendly_book_ahead_param = ssm.StringParameter(
            self, "calendlySourceEventBookAheadDays",
            string_value=calendly_book_ahead,
            parameter_name=parameter_path+"calendlySourceEventBookAheadDays"
        )
        calendly_book_ahead_param.apply_removal_policy(RemovalPolicy.DESTROY)
        CfnOutput(
            self, "calendlySourceEventBookAheadDaysParam",
            value=calendly_book_ahead_param.parameter_arn
        )

        calendly_event_id_param = ssm.StringParameter(
            self, "calendlySourceEventId",
            string_value=calendly_event_id,
            parameter_name=parameter_path+"calendlySourceEventId"
        )
        calendly_event_id_param.apply_removal_policy(RemovalPolicy.DESTROY)
        CfnOutput(
            self, "calendlySourceEventIdParam",
            value=calendly_event_id_param.parameter_arn
        )

        google_project_id_param = ssm.StringParameter(
            self, "googleCloudProjectId",
            string_value=google_project_id,
            parameter_name=parameter_path+"googleCloudProjectId"
        )
        google_project_id_param.apply_removal_policy(RemovalPolicy.DESTROY)
        CfnOutput(
            self, "googleCloudProjectIdParam",
            value=google_project_id_param.parameter_arn
        )

        calendly_source_bearer_token_param = ssm.StringParameter(
            self, "calendlySourceBearerToken",
            string_value=calendly_source_bearer_token,
            parameter_name=parameter_path+"calendlySourceBearerToken"
        )
        calendly_source_bearer_token_param.apply_removal_policy(RemovalPolicy.DESTROY)
        CfnOutput(
            self, "calendlySourceBearerTokenParam",
            value=calendly_source_bearer_token_param.parameter_arn
        )

        google_target_calendar_id_param = ssm.StringParameter(
            self, "googleTargetCalendarId",
            string_value=google_target_calendar_id,
            parameter_name=parameter_path+"googleTargetCalendarId"
        )
        google_target_calendar_id_param.apply_removal_policy(RemovalPolicy.DESTROY)
        CfnOutput(
            self, "googleTargetCalendarIdParam",
            value=google_target_calendar_id_param.parameter_arn
        )

        google_calendar_config_layer_bucket = s3.Bucket.from_bucket_name(
            self,
            "googleConfigBucket",
            google_calendar_config_layer_bucket_name
        )
        google_calendar_config_layer_code = lambda_.S3Code(
            google_calendar_config_layer_bucket,
            google_calendar_config_layer_file_name
        )
        google_calendar_config_layer = lambda_.LayerVersion(
            self, "googleCalendarConfigLayer",
            code=google_calendar_config_layer_code
        )
        CfnOutput(
            self, "googleCalendarConfigLayerOutput",
            value=google_calendar_config_layer.layer_version_arn
        )
