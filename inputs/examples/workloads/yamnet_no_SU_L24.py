#SOFTMAX NOT IMPLEMENTED YET!!!!
#is averpool 'W' 0 or 8 or what?????
workload = {
    24: {  # conv13_pw
        'equation': 'O[b][k][oy][ox]+=W[k][c][fy][fx]*I[b][c][ix][iy]',
        'dimension_relations': ['ix=1*ox+1*fx', 'iy=1*oy+1*fy'],
        'loop_dim_size': {'B': 1, 'K': 1024, 'C': 512, 'OY': 2, 'OX': 3, 'FY': 1, 'FX': 1, },
        'operand_precision': {'O': 16, 'O_final': 8, 'W': 8, 'I': 8},
        'operand_source': {'W': [], 'I': []},
        'constant_operands': ['W'],
        'operand_source_dimension_mapping': {'I': {'IX': 'OX', 'IY': 'OY', 'C': 'C'}},
        # 'spatial_mapping': {'D1': ('K', 16), 'D2': ('C', 16)},  # if you uncomment this, it is able to find some results.
        'core_allocation': 1,
        'memory_operand_links': {'O': 'O', 'W': 'I2', 'I': 'I1'}
    },
}
