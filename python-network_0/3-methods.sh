#!/bin/bash
# Displays the HTTP methods accepted by the server
curl -sI "$1" | grep "^Allow:" | cut -d' ' -f2-
