Names: Aditya Vikram Singh, Sahil Gupta

Bot Name: Astrominimax

Evaluation Function: We chose to create an evaluation function that considers two aspects of a state, the state cost (the present value of the state as defined by the difference between player 1's score and player 2's score, using scores() function) and the state potential (the potential score difference by measuring the number of 0's with adjacent sequences of 1's and -1's respectively, using squaring of potential sequence lengths). We weighted them equally in anticipation that we are only considering static features and thus we are not considering any other states per se, but only the current and future potential turnover.

Testing Boards:
- even_length_square_test: to check whether an empty 2x2 board has optimal score as (0,0) (obvious)
- odd_length_square_test: to check whether an empty 3x3 board has optimal score as (9,9) (played by hand, with insight from depth-limited optimizing)
- high_depth_low_breadth_test: to check whether an empty 4x3 board has optimal score as (18, 18) (played by hand, with insight from depth-limited optimizing)
- low_depth_high_breadth_test: to check whether an empty 3x4 board has optimal score as (9, 16) (played by hand, with insight from depth-limited optimizing)
- extreme_breadth_test: to check whether an empty 1x6 board has optimal score as (0, 0) (obvious for optimal agents)
- extreme_depth_test: to check whether an empty 6x1 board has optimal score as (0, 0) (obvious as there is only one possible move at every instance)
- high_depth_low_breadth_test_partial: to check whether a partially played 4x3 board has optimal score as (9, 9) (played by hand, with insight from depth-limited optimizing)
- low_depth_high_breadth_test_partial: to check whether a partially played 3x4 board has optimal score as (25, 9) (played by hand, with insight from depth-limited optimizing)

What is Working: 
- MinimaxAgent with minimax() implemented is working successfully
- MinimaxHeuristicAgent with minimax() and evaluation() implemented is working successfully
- MinimaxHeuristicPruneAgent with alpha-beta pruning minimax() implemented is working successfully