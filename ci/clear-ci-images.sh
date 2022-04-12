#!/usr/bin/env bash
# Remove all images created in a CI run
docker image rm --force ci_db:latest ci_test:latest ci_s3:latest
