def populate():
		solver_dict = {
		'spatial_order':1,
		'spatial_method':1,
		'quadrature_order':4,
		'quadrature_type':1,
		'nodes_xyz':[4,4,4],
		'num_groups':1,
		'num_materials':1,
		'x_cells_widths':[0.25, 0.25, 0.25, 0.25],
	 	'y_cells_widths':[0.25, 0.25, 0.25, 0.25],
		'z_cells_widths':[0.25, 0.25, 0.25, 0.25],
		'x_boundry_conditions':[2,2],
		'y_boundry_conditions':[2,2],
		'z_boundry_conditions':[2,2],
		'material_id': [[[0]*4]*4]*4,
		'quadrature_file':'quad_file',
		'xs_file':'xs_file',
		'srcfile':'src_4.dat',
		'converge_critical':1.e-12,
		'max_iterations':6000,
		'moments_converged':0,
		'converge_tolerence':1.e-10,
		'ichk':0,
		'ichk_tolerence':1.e-14,
		'momsum':0,
		'mompt':0,
		'qdflx':0
		};
		return solver_dict
'''
To create dictionary:
from dictionary_populate import populate
c = populate()
print(c)
'''
