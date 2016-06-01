import os

class Graph(object):
    # Initializing empty graph
    def __init__(self):
        self.adj_list = dict()    # Initial adjacency list is empty dictionary
        self.vertices = set()    # Vertices are stored in a set
        self.degrees = dict()    # Degrees stored as dictionary

    # Checks if (node1, node2) is edge of graph. Output is 1 (yes) or 0 (no).
    def isEdge(self,node1,node2):
        if node1 in self.vertices:        # Check if node1 is vertex
            if node2 in self.adj_list[node1]:    # Then check if node2 is neighbor of node1
                return 1            # Edge is present!

        if node2 in self.vertices:        # Check if node2 is vertex
            if node1 in self.adj_list[node2]:    # Then check if node1 is neighbor of node2
                return 1            # Edge is present!

        return 0                # Edge not present!

    # Add undirected, simple edge (node1, node2)
    def addEdge(self,node1,node2):

        # print('Called')
        if node1 == node2:            # Self loop, so do nothing
            # print('self loop')
            return
        if node1 in self.vertices:        # Check if node1 is vertex
            nbrs = self.adj_list[node1]        # nbrs is neighbor list of node1
            if node2 not in nbrs:         # Check if node2 already neighbor of node1
                nbrs.add(node2)            # Add node2 to this list
                self.degrees[node1] = self.degrees[node1]+1    # Increment degree of node1

        else:                    # So node1 is not vertex
            self.vertices.add(node1)        # Add node1 to vertices
            self.adj_list[node1] = {node2}    # Initialize node1's list to have node2
            self.degrees[node1] = 1         # Set degree of node1 to be 1

        if node2 in self.vertices:        # Check if node2 is vertex
            nbrs = self.adj_list[node2]        # nbrs is neighbor list of node2
            if node1 not in nbrs:         # Check if node1 already neighbor of node2
                nbrs.add(node1)            # Add node1 to this list
                self.degrees[node2] = self.degrees[node2]+1    # Increment degree of node2

        else:                    # So node2 is not vertex
            self.vertices.add(node2)        # Add node2 to vertices
            self.adj_list[node2] = {node1}    # Initialize node2's list to have node1
            self.degrees[node2] = 1         # Set degree of node2 to be 1

    # Give the size of the graph. Outputs [vertices edges wedges]
    #
    def size(self):
        n = len(self.vertices)            # Number of vertices

        m = 0                    # Initialize edges/wedges = 0
        wedge = 0
        for node in self.vertices:        # Loop over nodes
            deg = self.degrees[node]      # Get degree of node
            m = m + deg             # Add degree to current edge count
            wedge = wedge+deg*(deg-1)/2        # Add wedges centered at node to wedge count
        return [n, m, wedge]            # Return size info

    # Print the graph
    def output(self,fname,dirname):
        os.chdir(dirname)
        f_output = open(fname,'w')

        for node1 in list(self.adj_list.keys()):
            f_output.write(str(node1)+': ')
            for node2 in (self.adj_list)[node1]:
                f_output.write(str(node2)+' ')
            f_output.write('\n')
        f_output.write('------------------\n')
        f_output.close()

    def path(self, src, dest):
        """ implement your shortest path function here """
        shortest_path = []

        # Your code comes here
        q = list()
        visited = set()
        visited.add(src)
        dist = {};
        pred = {};
        dist[src] = 0;
        pred[src] = None
        q.append(src)
        while q:
            u = q.pop(0) #set u equal to first value in queue
            for v in (self.adj_list)[u]: #for every adjacent vertice of u
                if v not in visited: #check if it has been visited
                    visited.add(v) #if not add to visited set
                    pred[v] = u #set its predecessor to u
                    dist[v] = dist[u] + 1 #set its distance to 1 + its predecessors distance from src
                    q.append(v) #add to queue
                    if v == dest: #if dest was processed break out of loop
                        break
            if dest in visited: #if dest was visited break out of loop
                break
            if len(visited) == len(self.vertices): #if all vertices found break out of loop
                break
        start = dest;
        while start is not None: #start at the destination and work backwards
            shortest_path.insert(0, start)
            start = pred[start]
            
        return shortest_path
    
    def levels(self, src):
        """ implement your level set code here """
        level_sizes = [0,0,0,0,0,0,0]

        # Your code comes in here
        q = list()
        visited = set()
        visited.add(src)
        dist = {};
        pred = {};
        dist[src] = 0;
        pred[src] = None
        q.append(src)
        while q: 
            u = q.pop(0) #set u equal to first value in queue
            for v in (self.adj_list)[u]: #for every adjacent vertice of u
                if v not in visited: #check if it has been visited
                    visited.add(v) #if not add to visited set
                    pred[v] = u #set its predecessor to u
                    dist[v] = dist[u] + 1 #set its distance to 1 + distance of predecessor
                    q.append(v) #add to queue
                if len(visited) == len(self.vertices): #if all vertices found break
                    break
            if len(visited) == len(self.vertices): #if all vertices found break
                break
        for node in dist: #iterate through distance array and increment number of nodes at each distance
            if dist[node] == 0:
                level_sizes[0] = level_sizes[0] + 1
            elif dist[node] == 1:
                level_sizes[1] = level_sizes[1] + 1
            elif dist[node] == 2:
                level_sizes[2] = level_sizes[2] + 1
            elif dist[node] == 3:
                level_sizes[3] = level_sizes[3] + 1
            elif dist[node] == 4:
                level_sizes[4] = level_sizes[4] + 1
            elif dist[node] == 5:
                level_sizes[5] = level_sizes[5] + 1
            else:
                level_sizes[6] = level_sizes[6] + 1
                
        return level_sizes
