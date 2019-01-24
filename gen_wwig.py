import vol as v


g = v.IsoVolume()
g.assign_levels([0.3, 0.5])
g.generate_volumes('./ww-mesh.vtk', 'ww_val')
g.create_geometry(tag_groups=True, tag_for_viz=True)
g.write_geometry(sname='wwig.h5m')
g.write_geometry(sname='wwig.vtk')
