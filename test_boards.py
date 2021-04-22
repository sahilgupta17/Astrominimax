"""Test boards for Connect383

Place test boards in this module to help test your code.  Note that since connect383.GameState
stores board contents as a 0-based list of lists, these boards are reversed to they can be written
right side up here.

"""

boards = {}  # dictionary with label, test board key-value pairs

boards['choose_right'] = reversed([  
    [  0,  0 ],                       
    [ -1,  1 ],
    [ -1,  1 ] 
])

boards['choose_middle'] = reversed([  
    [ -1,  0,  0,  -1, -1 ],  
    [ -1,   1, -1,  1,  1 ],
    [  1,  -1,  1, -1,  1 ],
    [  1,   1, -1,  1, -1 ] 
])

boards['writeup_1'] = reversed([
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0, -1,  0,  0,  0 ],
    [  0,  0,  0,  1,  0,  0,  0 ],
    [  0,  1,  0, -1,  0,  1,  0 ]
])

boards['writeup_2'] = reversed([  
    [ -1,  1, -1, -1 ],                       
    [  1, -1,  1, -1 ],
    [  1, -2, -1,  1 ],
    [  1, -2,  1, -1 ] 
])

# 2x2 Board: optimal should be (0,0)
boards['even_length_square_test'] = reversed([
    [0,0],
    [0,0],  
]) 

# 3x3 Board: optimal should be (9,9)
boards['odd_length_square_test'] = reversed([
    [0,0,0],
    [0,0,0],
    [0,0,0],   
]) 

# 4x3 Board: optimal should be (18, 18)
boards['high_depth_low_breadth_test'] = reversed([
    [0,0,0],
    [0,0,0],
    [0,0,0], 
    [0,0,0],  
]) 

# 3x4 Board: optimal should be (9, 16)
boards['low_depth_high_breadth_test'] = reversed([
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],   
]) 

# 1x6 Board: optimal should be (0, 0)
boards['extreme_breadth_test'] = reversed([
    [0,0,0,0,0,0],
]) 

# 6x1 Board: optimal should be (0, 0)
boards['extreme_depth_test'] = reversed([
    [0],[0],[0],[0],[0],[0],  
]) 

# 4x3 Board (partially played): optimal should be (9, 9)
boards['high_depth_low_breadth_test_partial'] = reversed([
    [0,1,0],
    [-1,1,0],
    [-1,1,-1], 
    [1,-1,1],  
]) 

# 3x4 Board (partially played): optimal should be (25, 9)
boards['low_depth_high_breadth_test_partial'] = reversed([
    [0,0,0,0],
    [1,1,0,1],
    [1,-1,0,-1],   
]) 