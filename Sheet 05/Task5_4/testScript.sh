#!/usr/bin bash

otp="$(head -c 20 /dev/urandom)"

echo ${otp}