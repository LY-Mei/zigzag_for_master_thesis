#work on the commented lines and they will be different for each hardware(spatial mapping)
#SOFTMAX NOT IMPLEMENTED YET!!!! I think I will not????
#is averpool 'W' 0 or 8 or what?????
#Is K really 2??? It is 1000 in resnet18.
workload = {
    0: {  # conv1, 
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 16, 'C': 3, 'OY': 32, 'OX': 32, 'FY': 3, 'FX': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': []},
        'constant_operands': ['W'],
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 16), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    1: {  # conv2_1
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 16, 'C': 16, 'OY': 32, 'OX': 32, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [0]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 16), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    2: {  # conv2_2
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 16, 'C': 16, 'OY': 32, 'OX': 32, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [1]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 16), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    3: {  # Addition of layer 0 (residual path) and layer 2 (main path)
        'equation': 'O[b][g][oy][ox]=X[b][g][oy][ox]+Y[b][g][oy][ox]',
        'dimension_relations': [],
        'loop_dim_size': {'B': 1, 'G': 16, 'OY': 32, 'OX': 32},
        'operand_precision': {'O': 16, 'O_final': 8, 'X': 8, 'Y': 8},
        'operand_source': {'X': [0], 'Y': [2]},
        'constant_operands': [],
        'operand_source_dimension_mapping': {'X': {'OX': 'OX', 'OY': 'OY', 'G': 'K'}, 'Y': {'OX': 'OX', 'OY': 'OY', 'G': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('G', 16)},
        'memory_operand_links': {'O': 'O', 'X': 'I2', 'Y': 'I1'}
    }
    ,
    4: {  # conv2_3
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 16, 'C': 16, 'OY': 32, 'OX': 32, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [3]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'G'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 16), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    5: {  # conv2_4
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 16, 'C': 16, 'OY': 32, 'OX': 32, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [4]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 16), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    6: {  # Addition of layer 3 (residual path) and layer 5 (main path)
        'equation': 'O[b][g][oy][ox]=X[b][g][oy][ox]+Y[b][g][oy][ox]',
        'dimension_relations': [],
        'loop_dim_size': {'B': 1, 'G': 16, 'OY': 32, 'OX': 32},
        'operand_precision': {'O': 16, 'O_final': 8, 'X': 8, 'Y': 8},
        'operand_source': {'X': [3], 'Y': [5]},
        'constant_operands': [],
        'operand_source_dimension_mapping': {'X': {'OX': 'OX', 'OY': 'OY', 'G': 'G'}, 'Y': {'OX': 'OX', 'OY': 'OY', 'G': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('G', 16)},
        'memory_operand_links': {'O': 'O', 'X': 'I2', 'Y': 'I1'}
    }
    ,
    7: {  # conv2_5
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 16, 'C': 16, 'OY': 32, 'OX': 32, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [6]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'G'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 16), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    8: {  # conv2_6
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 16, 'C': 16, 'OY': 32, 'OX': 32, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [7]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 16), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    9: {  # Addition of layer 6 (residual path) and layer 8 (main path)
        'equation': 'O[b][g][oy][ox]=X[b][g][oy][ox]+Y[b][g][oy][ox]',
        'dimension_relations': [],
        'loop_dim_size': {'B': 1, 'G': 16, 'OY': 32, 'OX': 32},
        'operand_precision': {'O': 16, 'O_final': 8, 'X': 8, 'Y': 8},
        'operand_source': {'X': [6], 'Y': [8]},
        'constant_operands': [],
        'operand_source_dimension_mapping': {'X': {'OX': 'OX', 'OY': 'OY', 'G': 'G'}, 'Y': {'OX': 'OX', 'OY': 'OY', 'G': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('G', 16)},
        'memory_operand_links': {'O': 'O', 'X': 'I2', 'Y': 'I1'}
    }
    ,
    10: {  # conv3_1, stride 2
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=2*ox+1*fx', 'iy=2*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 32, 'C': 16, 'OY': 16, 'OX': 16, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [9]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'G'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    11: {  # conv3_2
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 32, 'C': 32, 'OY': 16, 'OX': 16, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [10]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    12: {  # conv3_1, parallel, stride 2
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=2*ox+1*fx', 'iy=2*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 32, 'C': 16, 'OY': 16, 'OX': 16, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [9]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'G'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    
    13: {  # Addition of layer 12 (residual path) and layer 11 (main path)
        'equation': 'O[b][g][oy][ox]=X[b][g][oy][ox]+Y[b][g][oy][ox]',
        'dimension_relations': [],
        'loop_dim_size': {'B': 1, 'G': 32, 'OY': 16, 'OX': 16},
        'operand_precision': {'O': 16, 'O_final': 8, 'X': 8, 'Y': 8},
        'operand_source': {'X': [12], 'Y': [11]},
        'constant_operands': [],
        'operand_source_dimension_mapping': {'X': {'OX': 'OX', 'OY': 'OY', 'G': 'K'}, 'Y': {'OX': 'OX', 'OY': 'OY', 'G': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('G', 32)},
        'memory_operand_links': {'O': 'O', 'X': 'I2', 'Y': 'I1'}
    }
    ,
    14: {  # conv3_3
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 32, 'C': 32, 'OY': 16, 'OX':16, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [13]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'G'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    15: {  # conv3_4
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 32, 'C': 32, 'OY': 16, 'OX': 16, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [14]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    16: {  # Addition of layer 13 (residual path) and layer 15 (main path)
        'equation': 'O[b][g][oy][ox]=X[b][g][oy][ox]+Y[b][g][oy][ox]',
        'dimension_relations': [],
        'loop_dim_size': {'B': 1, 'G': 32, 'OY': 16, 'OX': 16},
        'operand_precision': {'O': 16, 'O_final': 8, 'X': 8, 'Y': 8},
        'operand_source': {'X': [13], 'Y': [15]},
        'constant_operands': [],
        'operand_source_dimension_mapping': {'X': {'OX': 'OX', 'OY': 'OY', 'G': 'G'}, 'Y': {'OX': 'OX', 'OY': 'OY', 'G': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('G', 32)},
        'memory_operand_links': {'O': 'O', 'X': 'I2', 'Y': 'I1'}
    }
    ,
    17: {  # conv3_5
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 32, 'C': 32, 'OY': 16, 'OX': 16, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [16]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'G'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    18: {  # conv3_6
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 32, 'C': 32, 'OY': 16, 'OX': 16, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [17]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    19: {  # Addition of layer 16 (residual path) and layer 18 (main path)
        'equation': 'O[b][g][oy][ox]=X[b][g][oy][ox]+Y[b][g][oy][ox]',
        'dimension_relations': [],
        'loop_dim_size': {'B': 1, 'G': 32, 'OY': 16, 'OX': 16},
        'operand_precision': {'O': 16, 'O_final': 8, 'X': 8, 'Y': 8},
        'operand_source': {'X': [16], 'Y': [18]},
        'constant_operands': [],
        'operand_source_dimension_mapping': {'X': {'OX': 'OX', 'OY': 'OY', 'G': 'G'}, 'Y': {'OX': 'OX', 'OY': 'OY', 'G': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('G', 32)},
        'memory_operand_links': {'O': 'O', 'X': 'I2', 'Y': 'I1'}
    }
    ,
    20: {  # conv4_1, stride 2
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=2*ox+1*fx', 'iy=2*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 64, 'C': 32, 'OY': 8, 'OX': 8, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [19]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'G'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    21: {  # conv4_2
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 64, 'C': 64, 'OY': 8, 'OX': 8, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [20]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    22: {  # conv4_1, parallel, stride 2
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=2*ox+1*fx', 'iy=2*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 64, 'C': 32, 'OY': 8, 'OX': 8, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [19]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'G'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    23: {  # Addition of layer 22 (residual path) and layer 21 (main path)
        'equation': 'O[b][g][oy][ox]=X[b][g][oy][ox]+Y[b][g][oy][ox]',
        'dimension_relations': [],
        'loop_dim_size': {'B': 1, 'G': 64, 'OY': 8, 'OX': 8},
        'operand_precision': {'O': 16, 'O_final': 8, 'X': 8, 'Y': 8},
        'operand_source': {'X': [22], 'Y': [21]},
        'constant_operands': [],
        'operand_source_dimension_mapping': {'X': {'OX': 'OX', 'OY': 'OY', 'G': 'K'}, 'Y': {'OX': 'OX', 'OY': 'OY', 'G': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('G', 32)},
        'memory_operand_links': {'O': 'O', 'X': 'I2', 'Y': 'I1'}
    }
    ,
    24: {  # conv4_3
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 64, 'C': 64, 'OY': 8, 'OX': 8, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [23]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'G'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    25: {  # conv4_4
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 64, 'C': 64, 'OY': 8, 'OX': 8, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [24]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    26: {  # Addition of layer 23 (residual path) and layer 25 (main path)
        'equation': 'O[b][g][oy][ox]=X[b][g][oy][ox]+Y[b][g][oy][ox]',
        'dimension_relations': [],
        'loop_dim_size': {'B': 1, 'G': 64, 'OY': 8, 'OX': 8},
        'operand_precision': {'O': 16, 'O_final': 8, 'X': 8, 'Y': 8},
        'operand_source': {'X': [23], 'Y': [25]},
        'constant_operands': [],
        'operand_source_dimension_mapping': {'X': {'OX': 'OX', 'OY': 'OY', 'G': 'G'}, 'Y': {'OX': 'OX', 'OY': 'OY', 'G': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('G', 32)},
        'memory_operand_links': {'O': 'O', 'X': 'I2', 'Y': 'I1'}
    }
    ,
    27: {  # conv4_5
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 64, 'C': 64, 'OY': 8, 'OX': 8, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [26]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'G'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    28: {  # conv4_6
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 64, 'C': 64, 'OY': 8, 'OX': 8, 'FY': 3, 'FX': 3, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [27]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 32), 'D2': ('C', 2), 'D3': ('OX', 4), 'D4': ('OY', 4)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    29: {  # Addition of layer 26 (residual path) and layer 28 (main path)
        'equation': 'O[b][g][oy][ox]=X[b][g][oy][ox]+Y[b][g][oy][ox]',
        'dimension_relations': [],
        'loop_dim_size': {'B': 1, 'G': 64, 'OY': 8, 'OX': 8},
        'operand_precision': {'O': 16, 'O_final': 8, 'X': 8, 'Y': 8},
        'operand_source': {'X': [26], 'Y': [28]},
        'constant_operands': [],
        'operand_source_dimension_mapping': {'X': {'OX': 'OX', 'OY': 'OY', 'G': 'G'}, 'Y': {'OX': 'OX', 'OY': 'OY', 'G': 'K'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('G', 32)},
        'memory_operand_links': {'O': 'O', 'X': 'I2', 'Y': 'I1'}
    },
    30: {  # aver pool
        'equation': 'O[b][g][oy][ox]+=W[fx][fy]*I[b][g][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'G': 64, 'OY': 1, 'OX': 1, 'FX': 8, 'FY': 8},
        'operand_precision': {'O': 16, 'O_final': 8, 'I': 8, 'W': 0},
        'operand_source': {'W': [], 'I': [29]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'G': 'G'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('G', 32)},
        'memory_operand_links': {'O': 'O', 'I': 'I1', 'W': 'I2'}
    },
    31: {  # fc
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 10, 'C': 64, 'OY': 1, 'OX': 1, 'FY': 1, 'FX': 1},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [30]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'G'}},
        'core_allocation': 1,
        'spatial_mapping': {'D1': ('K', 10), 'D2': ('C', 2), 'D3': ('OX', 1), 'D4': ('OY', 1)},
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
}
