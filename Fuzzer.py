#! /usr/bin/env python
import re
import sys
input_fuzzer = sys.argv[1]
for line in sys.stdin:
    regex = re.sub(r"(?<==)[^&\s]+", input_fuzzer, line.strip())
    print(regex)
       