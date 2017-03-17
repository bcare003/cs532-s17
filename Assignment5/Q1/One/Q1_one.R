#Bryan Carey
#Due March 16, 2017

library(igraph)

#Reading in from .gml file
karateclub <- graph.famous("Zachary")

#Coloring of nodes, denoting Mr. Hi & John A., and the students
V(karateclub)$color[1] <- "red"
V(karateclub)$color[34] <- "red"
V(karateclub)$color[2:33] <- "blue"



