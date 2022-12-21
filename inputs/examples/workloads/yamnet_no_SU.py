#SOFTMAX NOT IMPLEMENTED YET!!!!
#is averpool 'W' 0 or 8 or what?????
workload = {
    0: {  # conv1, stride 2
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=2*ox+1*fx', 'iy=2*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 32, 'C': 1, 'OY': 32, 'OX': 48, 'FY': 3, 'FX': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': []},
        'constant_operands': ['W'],
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    1: {  # conv2_dw
        'equation': 'O[b][c][oy][ox]+=W[c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'C': 32, 'OY': 32, 'OX': 48, 'FX': 3, 'FY': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'I': 8, 'W': 0},
        'operand_source': {'W': [], 'I': [0]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'I': 'I1', 'W': 'I2'}
    }
    ,
    2: {  # conv2_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 64, 'C': 32, 'OY': 32, 'OX': 48, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [1]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    3: {  # conv3_dw, stride 2
        'equation': 'O[b][c][oy][ox]+=W[c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=2*ox+1*fx', 'iy=2*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'C': 64, 'OY': 16, 'OX': 24, 'FX': 3, 'FY': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [2]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    4: {  # conv3_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 128, 'C': 64, 'OY': 16, 'OX': 24, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [3]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    5: {  # conv4_dw
        'equation': 'O[b][c][oy][ox]+=W[c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'C': 128, 'OY': 16, 'OX': 24, 'FX': 3, 'FY': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [4]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    6: {  # conv4_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 128, 'C': 128, 'OY': 16, 'OX': 24, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [5]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    },
    7: {  # conv5_dw, stride 2
        'equation': 'O[b][c][oy][ox]+=W[c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=2*ox+1*fx', 'iy=2*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'C': 128, 'OY': 8, 'OX': 12, 'FX': 3, 'FY': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [6]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    8: {  # conv5_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 256, 'C': 128, 'OY': 8, 'OX': 12, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [7]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    9: {  # conv6_dw
        'equation': 'O[b][c][oy][ox]+=W[c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'C': 256, 'OY': 8, 'OX': 12, 'FX': 3, 'FY': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [8]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    },
    10: {  # conv6_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 256, 'C': 256, 'OY': 8, 'OX': 12, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [9]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    11: {  # conv7_dw, stride 2
        'equation': 'O[b][c][oy][ox]+=W[c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=2*ox+1*fx', 'iy=2*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'C': 256, 'OY': 4, 'OX': 6, 'FX': 3, 'FY': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [10]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    12: {  # conv7_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 512, 'C': 256, 'OY': 4, 'OX': 6, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [11]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    },
    13: {  # conv8_dw
        'equation': 'O[b][c][oy][ox]+=W[c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'C': 512, 'OY': 4, 'OX': 6, 'FX': 3, 'FY': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [12]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    14: {  # conv8_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 512, 'C': 512, 'OY': 4, 'OX': 6, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [13]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    15: {  # conv9_dw
        'equation': 'O[b][c][oy][ox]+=W[c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'C': 512, 'OY': 4, 'OX': 6, 'FX': 3, 'FY': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [14]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    },
    16: {  # conv9_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 512, 'C': 512, 'OY': 4, 'OX': 6, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [15]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    17: {  # conv10_dw
        'equation': 'O[b][c][oy][ox]+=W[c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'C': 512, 'OY': 4, 'OX': 6, 'FX': 3, 'FY': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [16]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    18: {  # conv10_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 512, 'C': 512, 'OY': 4, 'OX': 6, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [17]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    },
    19: {  # conv11_dw
        'equation': 'O[b][c][oy][ox]+=W[c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'C': 512, 'OY': 4, 'OX': 6, 'FX': 3, 'FY': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [18]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    20: {  # conv11_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 512, 'C': 512, 'OY': 4, 'OX': 6, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [19]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    21: {  # conv12_dw
        'equation': 'O[b][c][oy][ox]+=W[c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'C': 512, 'OY': 4, 'OX': 6, 'FX': 3, 'FY': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [20]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    },
    22: {  # conv12_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 512, 'C': 512, 'OY': 4, 'OX': 6, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [21]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    23: {  # conv13_dw, stride 2
        'equation': 'O[b][c][oy][ox]+=W[c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=2*ox+1*fx', 'iy=2*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'C': 512, 'OY': 2, 'OX': 3, 'FX': 3, 'FY': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [22]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
    ,
    24: {  # conv13_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 1024, 'C': 512, 'OY': 2, 'OX': 3, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [23]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    },
    25: {  # conv14_dw
        'equation': 'O[b][c][oy][ox]+=W[c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'C': 1024, 'OY': 2, 'OX': 3, 'FX': 3, 'FY': 3},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [24]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    },
    26: {  # conv14_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 1024, 'C': 1024, 'OY': 2, 'OX': 3, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [25]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    },
    27: {  # aver pool
        'equation': 'O[b][g][oy][ox]+=W[fx][fy]*I[b][g][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'G': 1024, 'OY': 1, 'OX': 1, 'FX': 3, 'FY': 2},
        'operand_precision': {'O': 16, 'O_final': 8, 'I': 8, 'W': 0},
        'operand_source': {'W': [], 'I': [26]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'G': 'K'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'I': 'I1', 'W': 'I2'}
    },
    28: {  # fc
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 512, 'C': 1024, 'OY': 1, 'OX': 1, 'FY': 1, 'FX': 1},
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': [27]},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'G'}},
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    }
}
