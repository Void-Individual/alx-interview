#!/usr/bin/python3
"""Test Module"""

import sys

output_list = [
    "68.249.9.20 - [2017-02-05 23:31:22.452556] \"GET /projects/260 HTTP/1.1\" 200 711",
    "Hello",
    "99.196.100.39 - [2017-02-05 23:31:22.954433] \"GET /projects/260 HTTP/1.1\" 401 658",
    "128.230.61.246 - [2017-02-05 23:31:23.258076] \"GET /projects/260 HTTP/1.1\" Hello 292",
    "116.82.223.35 - [2017-02-05 23:31:24.112360] \"GET /projects/260 HTTP/1.1\" 301 842",
    "Holberton - [2017-02-05 23:31:25.003550] \"GET /projects/260 HTTP/1.1\" 400 12",
    "7.179.133.121 - [2017-02-05 23:31:25.003550] \"GET /projects/260 HTTP/1.1\" 400 12",
    "188.213.11.218-[2017-02-05 23:31:21.690755] \"GET /projects/260 HTTP/1.1\" 401 1000",
    "128.230.61.246 - [2017-02-05 23:31:23.258076] \"GET /projects/260 HTTP/1.1\" 301 292"
]

# Write each string to stdout and flush
for line in output_list:
    sys.stdout.write(line + "\n")  # Add newline character to match typical print behavior
    sys.stdout.flush()
