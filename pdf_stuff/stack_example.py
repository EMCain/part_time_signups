# http://stackoverflow.com/questions/18970491/parsing-a-pretty-printed-table-into-python-objects

likes_and_dislikes="""

+------------------------------------+-----------------------------------+
| likes                              | dislikes                          |
+------------------------------------+-----------------------------------+
| Meritocracy                        | Favoritism, ass-kissing, politics |
+------------------------------------+-----------------------------------+
| Healthy debates and collaboration  | Ego-driven rhetoric, drama and FUD|
|                                    | to get one's way                  |
+------------------------------------+-----------------------------------+
| Autonomy given by confident leaders| Micro-management by insecure      |
| capable of attracting top-tier     | managers compensating for a weak, |
| talent                             | immature team                     |
+------------------------------------+-----------------------------------+ """

import re
likes,dislikes = [],[] # initialize a pair of arrays that will hold the final answer
pairs = re.split("\+-*\+-*\+\n?",likes_and_dislikes)[2:-1] #Drop the header and the tail # split into "rows" of table
# rows are separated by a line in the form +------+------+\n

for p in pairs: # p is one "row" of the "table" regardless of how many lines are in it
  like,dislike = [],[] # initialize a pair of arrays that will eventually each be strung together into a single "cell" of the table
  for l in p.split('\n'): # for each line in the "row" (p)
    pair = l.split('|') # pair is an array containing the line split up by cell (first entry is '' I think, it's to the left of initial |)
    if len(pair) > 1:
      # Not a blank line
      like.append(pair[1].strip()) # 1 because pair[0] == ''. The array "like" gets another entry 
      dislike.append(pair[2].strip()) # 
  if len(like) > 0:
    likes.append(" ".join(like)) # stick together all the strings in "like" to create a single long string, then add this to the end of "likes"
  if len(dislike) > 0:
    dislikes.append(" ".join(dislike))
# likes and dislikes are now both arrays of strings, one per "cell". 	
	
from pprint import pprint
print "Likes:"
pprint(likes,indent=4)
print "Dislikes:"
pprint(dislikes,indent=4)
print "A set of paired likes and dislikes"
pprint(zip(likes,dislikes),indent=4)


