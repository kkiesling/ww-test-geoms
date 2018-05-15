from pymoab import core, types
from pymoab.rng import Range

def intersection(lst1, lst2):
    matches = []
    diffs = []
    for value in lst1:
        if value in lst2:
            matches.append(value)
        else:
            diffs.append(value)

    return matches, diffs

vol = core.Core()
vol.load_file("./tmp/vols/2-0.stl")
vroot = vol.get_root_set()
v_all_verts = vol.get_entities_by_type(vroot, types.MBVERTEX)

s1 = core.Core()
s1.load_file("./tmp/cont/c-4.stl")
sroot = s1.get_root_set()
s_all_verts = s1.get_entities_by_type(sroot, types.MBVERTEX)

# s_coords = []
# for v in s_all_verts:
#     s_coords.append(tuple(s1.get_coords(v)))

v_coords = []
for v in v_all_verts:
    v_coords.append(tuple(vol.get_coords(v)))

diff = []
for v in s_all_verts:
    if tuple(s1.get_coords(v)) not in v_coords:
        diff.append(v)

# get the connected set of triangles that make the single surf
tris = s1.get_adjacencies(diff, 2, op_type=1)
surf = s1.create_meshset()
s1.add_entities(surf, tris)

# write to file
r_surf = Range(surf)
s1.write_file("diffs.stl", r_surf)



