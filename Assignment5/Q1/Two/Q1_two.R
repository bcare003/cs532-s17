#Bryan Carey
#Due March 16, 2017

library(igraph)

#Reading in from .gml file
karateclub <- graph.famous("Zachary")

#Coloring of nodes, denoting Mr. Hi & John A., and the students
V(karateclub)$color[1] <- "red"
V(karateclub)$color[34] <- "red"
V(karateclub)$color[2:33] <- "blue"

#edge betweenness
karateclubsplit <-edge.betweenness.community(karateclub)

#found from 
mods <- sapply(
  0:ecount(karateclub), function(i){ 
    karateclub2 <- delete.edges(karateclub, karateclubsplit$removed.edges[seq(length=i)]) 
    cl <- clusters(karateclub2)$membership
    if(no.clusters(karateclub2)==2){
      plot(karateclub2,)}})


