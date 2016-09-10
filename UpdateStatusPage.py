#!/usr/bin/env python

from config import *
from statuspage import statuspage
from cStringIO import StringIO
import sys


def lambda_handler(event, conte):
    sys.stdout = capture = StringIO()
    statuspage.run_update(GITHUB_REPO_NAME, GITHUB_API_TOKEN, GITHUB_ORGANIZATION)
    sys.stdout = sys.__stdout__

    return capture.getvalue()
