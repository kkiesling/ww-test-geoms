import vol as v

N = 4
min_val = 10.
max_val = 3400.
f = 'test-mesh-expanded.vtk'
data = 'value'
db = 'tmp'

g = v.IsoVolume()
g.generate_levels(N, min_val, max_val, log=False)
g.generate_volumes(f, data, dbname=db)
g.create_geometry(tag_groups=True, tag_for_viz=True)
g.write_geometry(sname='vols.h5m')
g.write_geometry(sname='vols.vtk')
