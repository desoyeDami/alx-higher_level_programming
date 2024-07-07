# 0x10. Python - Network #0

## Description
This project focuses on the basics of HTTP (HyperText Transfer Protocol) and how to interact with web servers using `curl` and Python. You will learn how to construct HTTP requests, read URLs, understand HTTP response codes, and manage cookies. The tasks involve writing Bash scripts to make HTTP requests and a Python function to find a peak in a list of unsorted integers.

## Learning Objectives
At the end of this project, you should be able to explain the following concepts without assistance:
- What a URL is
- What HTTP is
- How to read a URL
- The scheme for an HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with `curl`
- What happens when you type `google.com` in your browser (Application level)

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- A `README.md` file at the root of the project folder is mandatory
- All scripts will be tested on Ubuntu 20.04 LTS
- All Bash scripts should be exactly 3 lines long
- All files should end with a new line
- All files must be executable
- The first line of all Bash scripts should be `#!/bin/bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose
- All `curl` commands must use the `-s` option (silent mode)
- All Python files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- The first line of all Python files should be `#!/usr/bin/python3`
- Your code should use `pycodestyle` (version 2.8.*)
- All modules should be documented
- All classes should be documented
- All functions (inside and outside a class) should be documented
- A documentation is a real sentence explaining the purpose of the module, class, or method

## Tasks

### 0. cURL body size
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.

**File:** `0-body_size.sh`

### 1. cURL to the end
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response (only if the status code is 200).

**File:** `1-body.sh`

### 2. cURL Method
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

**File:** `2-delete.sh`

### 3. cURL only methods
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

**File:** `3-methods.sh`

### 4. cURL headers
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable `X-School-User-Id` must be sent with the value `98`.

**File:** `4-header.sh`

### 5. cURL POST parameters
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response. Variables `email` and `subject` must be sent with the values `test@gmail.com` and `I will always be here for PLD`, respectively.

**File:** `5-post_params.sh`

### 6. Find a peak
Write a function that finds a peak in a list of unsorted integers.

**File:** `6-peak.py`

## Repository
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x10-python-network_0`
- Files:
  - `0-body_size.sh`
  - `1-body.sh`
  - `2-delete.sh`
  - `3-methods.sh`
  - `4-header.sh`
  - `5-post_params.sh`
  - `6-peak.py`
  - `6-peak.txt`

