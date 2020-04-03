
import collections
import pprint

with open ('mobydick.txt', 'r') as f:
    count_characthers = collections.Counter(f.read())
    s =pprint.pformat(count_characters)
#print(count_characters)
print(s)


             
