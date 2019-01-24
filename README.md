# Simple test geometries

Geometries that can be used for testing MCNP particle tracking implementation

## Generating the WWIG

1. Generate a mesh with `gen_wwmesh.py` ( `ww-mesh.h5m` )
2. Generate isosurface geom with `gen_wwig.py` ( `wwig.h5m`)

Notes:

* Must have at least 2 isosurface levels (current limitation of tool).
* to get viewable file: `mbconvert file.h5m file.vtk`

## Transport Geometry

* Created in Trelis.
* All vacuum materials.

File for transport: `transport-geom.h5m`
