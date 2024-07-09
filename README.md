# prim-algorithm
 
The prim algorithm is util for calculate min distance in graph where the edges has weight.

Example.: We have a graph 2D where -1 is obstacle in graph and not don't go to point.

graph = [

[1,1,1,1],

[3,-1,-1,-1],

[5,0,2,0],

[8,2,8,1],

[9,-1,-1,1]

]

First, we build our graph to a more sophisticated structure. We assign the distance from the starting point to zero, as it starts there, so there is no cost.

Then we build our system for queuing the graph elements.

After that, we can make the algorithm go through the queue, always looking for the minimum distance, from the left, right, top and bottom. After finding, determine who the predecessor of that point is and add the distance traveled with the new distance from the point.

Target is the last element in graph, then value is 1 or your position is [4,3]

The min distance then [0,0] (1) for [4,3] (1) is 12.

Initialize algorithm in [0,0] or your source where is different -1 and your target destination [4,3] where is different -1.

Then verify position left, right, top and bottom lowest cost edge.