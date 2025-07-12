#! /usr/bin/env python
import re
import sys
banner='''
 _______  _______  _______           _______  _______ 
(  ____ )(  ____ \(  ____ \|\     /|/ ___   )/ ___   )
| (    )|| (    \/| (    \/| )   ( |\/   )  |\/   )  |
| (____)|| (__    | (__    | |   | |    /   )    /   )
|     __)|  __)   |  __)   | |   | |   /   /    /   / 
| (\ (   | (      | (      | |   | |  /   /    /   /  
| ) \ \__| (____/\| )      | (___) | /   (_/\ /   (_/\
|/   \__/(_______/|/       (_______)(_______/(_______/
                                                      
'''
print(banner)

input_fuzzer = sys.argv[1]
for line in sys.stdin:
    regex = re.sub(r"(?<==)[^&\s]+", input_fuzzer, line.strip())
    print(regex)
       
