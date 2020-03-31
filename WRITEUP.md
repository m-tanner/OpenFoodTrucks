# Command Line MVP to Web Application

Much of what I discuss here comes from:

- https://www.educative.io/courses/grokking-the-system-design-interview
- https://lethain.com/introduction-to-architecting-systems-for-scale/

In the context of having something like the following (flowing from top to bottom):

- a client (where there are millions concurrent clients)
    - users go to website (say, www.show-open-foodtrucks.com)
    - users are presented with open food trucks in pages of ten
- load balancing layer
- web service layer
- load balancing layer
- application layer (with a cache)
- load balancing layer
- database layer (currently provided by Socrata)

The result for each user would only change when a food truck has opened or closed. With a cursory glance at 
https://data.sfgov.org/Economy-and-Community/Mobile-Food-Schedule/jjew-r69b/data
it seems like these changes only occur on the hour. This means that our application would benefit from a cache. 

For example, no matter how many users query in a given hour (given my above assumption that food trucks only open or close on the hour),
ever user is asking to view the same result. There would be no need to query the database more often than once an hour, 
provided the cache is available to all the servers needing to access the cache. On the other hand, each server could just as well
query the database (resulting in a number of database queries equal to the number of servers once per hour) and then keep the 
results in memory. The cache could even be pre-computed if Socrata's data changed infrequently enough.
