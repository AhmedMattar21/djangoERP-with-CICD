#!/bin/bash

if curl -I "http://127.0.0.1:8000" | grep -i "OK"
then
    exit 0
else
    exit 1
fi
