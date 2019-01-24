from pyne.mesh import Mesh, NativeMeshTag, MetadataTag, ComputedTag
import numpy as np

xcoords = np.linspace(-12., 12., num=25, endpoint=True)
ycoords = np.linspace(-12., 12., num=25, endpoint=True)
zcoords = np.linspace(-12., 12., num=25, endpoint=True)
coords = [xcoords, ycoords, zcoords]

m = Mesh(structured_coords=coords, structured=True, mats=None)
m.t = NativeMeshTag(size=1, default=0.01, mesh=m, name='ww_val')

for i in m.iter_ve():
    c = m.ve_center(i)
    if (-8. < c[0] < 8.) and (-8. < c[1] < 8.) and (-8. < c[2] < 8.):
        m.t[i] = .5
    if (-4. < c[0] < 4.) and (-4. < c[1] < 4.) and (-4. < c[2] < 4.):
        m.t[i] = 1.0


m.write_hdf5('ww-mesh.h5m')
