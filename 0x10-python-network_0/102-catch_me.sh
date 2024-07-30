#!/bin/bash
# This script that makes a request to a url that causes the server to respond with a message containing You got me!, in the body of the response.
curl -s -X POST -d "You got me!" http://0.0.0.0:5000/catch_me
