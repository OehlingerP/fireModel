#' Calculates the area burned in the fire model. 
#' 
#' @param mat matrix; binary matrix where 1's indicate trees
#' @description
#' The fire model explains the spread of wildfires. The function area_burned() 
#'    calculates the total area burned in the model. In the model you define a 
#'    tree density and then you randomly populate a matrix with 0's and 1's 
#'    given the tree density. The fire than spreads from the fire line (first 
#'    column) to other trees if they border a burning tree. Fire can spread up/
#'    down, left/right but not diagonally.

area_burned <- function( mat ) {
  
  # find the index of trees in the matrix
  pos <- which(mat == 1, arr.ind = TRUE) # array index is an extremely useful argument for this
  
  # calculate the manhatten distance between trees trees are connected if the 
  # manhatten distance equals 1. Manhattan distance is super simple: see for 
  # example https://de.wikipedia.org/wiki/Manhattan-Metrik
  distance_mat <- as.matrix( dist( pos, method = "manhattan", diag = T ) )
  distance_mat[ upper.tri( distance_mat ) ] <- 0
  
  # create edges (how nodes (pos) are connected)
  edge <- which( distance_mat == 1, arr.ind = TRUE )
  
  # create graph and find components
  # create a graph/network of trees that are connected (we stored the connections in edge)
  graph <- igraph::graph_from_edgelist( edge, directed = FALSE )
  
  # find components of graph using the igraph package
  comp <- igraph::components( graph )
  
  # find components that are hit by fire
  # the part which( pos[ , 2 ] == 1 ) refers to trees in the first column of
  # the matrix as only those are hit initially by the fire
  # comp$membership assigns each tree to a component (group) of the network
  comp_burned <- unique( comp$membership[ which( pos[ , 2 ] == 1 ) ] )
  
  # calculate area burned in percent
  # comp$csize is the size of each component
  area_burned <- sum( comp$csize[ comp_burned ] ) / sum( mat ) * 100
  
  return( area_burned )
  
}

#' simulate the spread of wildfires

  # install and load packages
  packages_to_load <- c( "ggplot2", "data.table", "igraph" )
  
  for( PACK in packages_to_load ){
    
    if( system.file( package = PACK ) == "" ) install.packages( PACK )
    library( PACK, character.only = T )
    
  }

  set.seed( 20230526 )

  # create matrix to store results
  df_store <- as.data.frame( matrix( 0, nrow = 100, ncol = 99 ) )
  
  time <- numeric( 99 )
  
  # define matrix/forest size
  matrix_size <- 50
  
  for( density in 1:99 ){ # loop through each density
    
    print( density )
    
    # save time for each step
    start_density <- Sys.time()
    
    for( i in 1:100 ){ # run simulation 100 times for each density
      
      # populate grid with trees
      mat <- matrix( sample( c( 0, 1 ),
                             replace = TRUE,
                             size = matrix_size^2,
                             prob = c( 1-density/100,
                                       density/100 ) ),
                     ncol = matrix_size )
    
      # run area_burned() see function above and store result
      df_store[ i, density ] <- area_burned( mat )
        
    }
    
    # store time it took to run simulation for one specific density
    time[ density ] <- difftime( Sys.time(), start_density, units = "mins" )
    
    
  }
  
  plot( time*60)
  
  plot( colMeans( df_store ) )
  
  # # store results
  # save( df_store, time, file = "simulation_and_time.Rda" )
  # 
  # # reformat data for plotting (I'll use ggplot2)
  # colnames( df_store ) <- 1:99
  # dt <- data.table::melt( as.data.table( df_store ) )
  # dt[ , variable:=as.numeric( variable ) ]
  # write.csv( na.omit( dt ), file = "data.csv" )
  # 
  # # calculate mean and standard deviation
  # dt <- dt[ , .("mean" = mean(value,na.rm=T), "sd" =sd(value,na.rm=T)), by=variable]
  # 
  # # plot results
  # plot <- ggplot( dt, aes( x = variable ) ) +
  #   geom_ribbon( aes( ymin = mean-sd, ymax = mean+sd ), alpha = 0.2 ) +
  #   geom_line( aes( y = mean ) )
  
  

    