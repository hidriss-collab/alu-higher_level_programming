#!/bin/bash
# Sends POST parameters
curl -sX POST \
-d "email=test@gmail.com" \
-d "subject=I will always be here for PLD" \
"$1"
