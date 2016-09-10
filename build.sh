#!/usr/bin/env bash

rm UpdateStatusPage.zip
cd $VIRTUAL_ENV/lib/python2.7/site-packages
zip -r /tmp/UpdateStatusPage.zip *
cd -
zip -g /tmp/UpdateStatusPage.zip *
mv /tmp/UpdateStatusPage.zip .
