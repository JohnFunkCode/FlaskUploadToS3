#!/usr/bin/env bash
cf update-user-provided-service s3bucket -p '{"S3_BUCKET":"jpf-python-datastore","S3_ACCESS_KEY":"YourAccessKeyHere","S3_SECRET_KEY":"YourSecreKeyHere"
cf restage flask-s3-upload