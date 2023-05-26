library( tidyr )
library( dplyr )
library( ggplot2 )
library( data.table )

# initialize matrix
density     <- 62
matrix_size <- 200

# create forest grid
set.seed( 20230508 )
mat <- matrix( sample( c( 0, 1 ),
                       replace = TRUE,
                       size = matrix_size^2,
                       prob = c( 1-density/100,
                                 density/100 ) ),
               ncol = matrix_size )

# convert to long format as it is easier to use when plotting
df <- as.data.frame( mat ) %>%
  mutate( row_idx = 1:matrix_size ) %>%
  pivot_longer( -row_idx, names_to = "col_idx" ) %>%
  mutate( col_idx = as.numeric( gsub( "V", "", col_idx ) ),
          time = 0,
          row_col = paste( row_idx, col_idx ) )

saveRDS( df, file = "Fire Model Data/density62/draw_0.Rds" )

# start fire
df <- df %>%
  mutate( value = ifelse( col_idx == 1 & value == 1, 0.8, value ),
          time = 1 )

saveRDS( df, file = "Fire Model Data/density62/draw_1.Rds" )

on_fire <- df
TIME <- 1
while( nrow( on_fire ) > 0 ){

  TIME <- TIME + 1
  print( TIME )

  # find burning trees
  on_fire <- df[ df$value == 0.8, ]

  # find bordering trees of the trees that are currently burning
  # move left/right
  right_col <- on_fire$col_idx + 1
  left_col <- on_fire$col_idx - 1
  right_row <- left_row <- on_fire$row_idx
  # move up/down
  up_col <- down_col <- on_fire$col_idx
  up_row <- on_fire$row_idx + 1
  down_row <- on_fire$row_idx - 1

  # define trees catching fire
  on_fire <- data.frame( row_idx = c( right_row, left_row, up_row, down_row ),
                         col_idx = c( right_col, left_col, up_col, down_col ) )

  on_fire <- on_fire %>%
    filter( row_idx > 0, col_idx > 0 ) %>%
    unique() %>%
    mutate( row_col = paste( row_idx, col_idx ) )

  # burn down already burning trees
  df <- df %>%
    mutate( value = ifelse( value != 1 & value > 0.3, value - 0.2, value ),
            time = TIME )

  # assign newly burning trees
  df[ df$value == 1 &
      df$row_col %in% on_fire$row_col, "value" ] <- 0.8

  saveRDS( df, file = paste0( "Fire Model Data/density62/draw_", TIME, ".Rds" ) )

}

# Converts a matrix of trees into an adjacency matrix where two trees
#  are connected if they are neighbors.

matrix_to_adjacency <- function(matrix) {

  n_trees <- sum(matrix)
  tree_indices <- which(matrix == 1, arr.ind = TRUE)
  adj_matrix <- matrix(0, n_trees, n_trees)
  dist_matrix <- as.matrix(dist(tree_indices, method = "manhattan")) # Compute Manhattan distance matrix
  adj_matrix[dist_matrix <= 1] <- 1 # Set adjacency matrix entries to 1 for neighboring trees
  return(adj_matrix)
}

my_matrix <- matrix(c(1,0,1,0,0,1,1,1,0,1,0,0), nrow=3, ncol=4, byrow=TRUE)
adj_matrix <- matrix_to_adjacency(my_matrix)

# area burned simulation
df_out <- data.frame( density = rep( 1:70, each = 100 ),
                      draw = rep( 1:100, 70 ),
                      area_burned = NA )

set.seed( 20230508 )

for( DRAW in 1:nrow( df ) ){

  print( DRAW )

  temp_density <- df_out[ DRAW, "density" ]

  matrix_size <- 100

  # create forest grid
  mat <- matrix( sample( c( 0, 1 ),
                         replace = TRUE,
                         size = matrix_size^2,
                         prob = c( 1-temp_density/100,
                                   temp_density/100 ) ),
                 ncol = matrix_size )

  # convert to long format as it is easier to use when plotting
  df_init <- as.data.frame( mat ) %>%
    mutate( row_idx = 1:matrix_size ) %>%
    pivot_longer( -row_idx, names_to = "col_idx" ) %>%
    mutate( col_idx = as.numeric( gsub( "V", "", col_idx ) ),
            row_col = paste( row_idx, col_idx ) )

  df <- df_init %>%
    mutate( value = ifelse( col_idx == 1 & value == 1, 0.8, value ) )

  on_fire <- df
  i <- 1
  while( nrow( on_fire ) > 0 ){

    i <- i + 1

    # find burning trees
    on_fire <- df[ df$value == 0.8, ]

    # find bordering trees of the trees that are currently burning
    # move left/right
    right_col <- on_fire$col_idx + 1
    left_col <- on_fire$col_idx - 1
    right_row <- left_row <- on_fire$row_idx
    # move up/down
    up_col <- down_col <- on_fire$col_idx
    up_row <- on_fire$row_idx + 1
    down_row <- on_fire$row_idx - 1

    # define trees catching fire
    on_fire <- data.frame( row_idx = c( right_row, left_row, up_row, down_row ),
                           col_idx = c( right_col, left_col, up_col, down_col ) )

    on_fire <- on_fire %>%
      filter( row_idx > 0, col_idx > 0 ) %>%
      unique() %>%
      mutate( time = TIME,
              row_col = paste( row_idx, col_idx ) )

    # burn down already burning trees
    df <- df %>%
      mutate( value = ifelse( value != 1 & value > 0.3, value - 0.2, value ) )

    # assign newly burning trees
    df[ df$value == 1 & df$row_col %in% on_fire$row_col, "value" ] <- 0.8

  }

  # calculate area burned
  df_out[ DRAW, "area_burned" ] <- round( nrow( df %>% filter( value < 1, value > 0 ) ) / sum( df_init$value ) * 100, 2 )

}

saveRDS( df_out, file = "fire_model_output_simulation_varying_density.Rds" )
ggplot( fire_model_output_denstity62%>% filter( time == 200
                                                ), aes( x = col_idx, y = row_idx, fill = as.factor( value ) ) ) +
  geom_raster() +
  scale_fill_manual( values = my_cols ) +
  scale_y_continuous( expand = c( 0, 0 ) ) +
  scale_x_continuous( expand = c( 0, 0 ) ) +
  #geom_vline( xintercept = 0, color = "red", lwd = 1.5 ) +
  theme_empty
