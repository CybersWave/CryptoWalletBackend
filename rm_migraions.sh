#! /bin/bash

set -e

find . -path "*migrations*" -not -regex ".*__init__.py" -a -not -regex ".*migrations" | xargs rm -rf
