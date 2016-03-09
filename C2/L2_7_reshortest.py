__author__ = 'Hernan Y.Ke'
import re

# greey and non-greedy matching
greedyre = re.compile(r'\"(.*)\"')

nongreedyre=re.compile(r'\"(.*?)\"')


print(greedyre.findall('longlong"first"longlong"second"'))
print(nongreedyre.findall('longlong"first"longlong"second"'))