#!/bin/bash
tar \
--exclude='infrastructure/.venv' \
--exclude='infrastructure/proton-inputs.json' \
--exclude='infrastructure/cdk.out' \
-zcvf ./tarred/calendlyGoogleSyncEnvironTemplateBundle.tar.gz infrastructure schema
