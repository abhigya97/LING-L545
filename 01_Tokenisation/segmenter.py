import sys
import re
line = sys.stdin.readline()

def segmenter(line):
    line = re.sub(r'(\. )', r'\g<1>\n', line)
    return line
    

while line:
    line = segmenter(line)
    sys.stdout.write(line)
    line = sys.stdin.readline()