#!/usr/bin/env python3

import aws_cdk as cdk

from calendly_google_sync_environment.calendly_google_sync_environment_stack import CalendlyGoogleSyncEnvironmentStack


app = cdk.App()
CalendlyGoogleSyncEnvironmentStack(app, "calendly-google-sync-environment")

app.synth()
