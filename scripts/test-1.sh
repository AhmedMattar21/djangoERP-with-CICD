#!/bin/bash

if curl -I "http://127.0.0.1:8000" | grep -i "OK"
then
    return 0
else
    return 1
fi
