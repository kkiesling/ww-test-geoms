from pyne.mesh import Mesh, IMeshTag, MetadataTag, ComputedTag
import numpy as np

xcoords = np.linspace(-30., 30., num=30, endpoint=True)
ycoords = np.linspace(-20., 40., num=30, endpoint=True)
zcoords = np.linspace(-10., 50., num=30, endpoint=True)
coords = [xcoords, ycoords, zcoords]

m = Mesh(structured_coords=coords, structured=True, mats=None)
m.value = IMeshTag(size=1, dtype=float)

idx = 0
values = []
for x in xcoords[1:]:
    for y in ycoords[1:]:
        for z in zcoords[1:]:
            val = abs(x*z) + abs(y*z)
            values.append(val)

            idx += 1

m.value[:] = values

m.write_hdf5('test-mesh.h5m')
