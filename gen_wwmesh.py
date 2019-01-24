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
    if (-5. < c[0] < 5.) and (-10. < c[1] < 10.) and (-5. < c[2] < 5.):
        m.t[i] = 0.5

m.write_hdf5('ww-mesh.h5m')
