#!/bin/bash

otp="$(head -c 500 /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9~!@#$%^&*_-' | fold -w 20 | head -n 1)"

java -jar ./out/artifacts/OTPServer_jar/OTPServer.jar ${otp} &

java -jar ./out/artifacts/OTPClient_jar/OTPClient.jar ${otp} &