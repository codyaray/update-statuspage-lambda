# UpdateStatusPage API

Building on the open source [statuspage](https://github.com/jayfk/statuspage) freely hosted by Github Pages,
the UpdateStatusPage API uses Amazon to automatically update your statuspage after a status change.
You can let Amazon host this for you and save the $39/year.

## Overview

This project implements a simple webhook built on Amazon Lambda and API Gateway. You configure your Github
(or Bitbucket) repo to hit this webhook when any issues are opened, updated, or closed. The Lambda will
automatically run the `statuspage update` command for you.

## Configuration

Checkout `config.py` and update for your github repo, token, and (optional) organization.

## Deploy

Go ahead and create a virtualenv. You know you wanna.

    virtualenv /tmp/env
    . /tmp/env/bin/activate
    pip install -r requirements.txt

To create the [deployment package](http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)
for Lambda, you have to install all dependencies from the virtualenv. Fortunately, we've already built a
handy little script to create this deployment package for you.

    ./build.sh

This creates the file UpdateStatusPage.zip which you can upload using the CLI or the Web Console.
