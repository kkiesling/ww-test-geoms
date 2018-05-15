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

v2 = core.Core()
v2.load_file("./tmp/vols/2-0.stl")
v2r = v2.get_root_set()
v2_all_verts = v2.get_entities_by_type(v2r, types.MBVERTEX)

v3 = core.Core()
v3.load_file("./tmp/vols/3-0.stl")
v3r = v3.get_root_set()
v3_all_verts = v3.get_entities_by_type(v3r, types.MBVERTEX)

v2_coords = []
for v in v2_all_verts:
    v2_coords.append(tuple([tuple(v2.get_coords(v)),v]))

v3_coords = []
for v in v3_all_verts:
    v3_coords.append(tuple(v3.get_coords(v)))

match_eh = []
diff_eh = []
for v_set in v2_coords:
    if v_set[0] in v3_coords:
        match_eh.append(v_set[1])
    else:
        diff_eh.append(v_set[1])

# get the connected set of triangles that make the single surf
diff_tris = v2.get_adjacencies(diff_eh, 2, op_type=1)
diff_surf = v2.create_meshset()
v2.add_entities(diff_surf, diff_tris)

# write to file
r_surf = Range(diff_surf)
v2.write_file("diffs-v23.stl", r_surf)

# get the connected set of triangles that make the single surf
match_tris = v2.get_adjacencies(match_eh, 2, op_type=1)
match_surf = v2.create_meshset()
v2.add_entities(match_surf, match_tris)

# write to file
r_surf = Range(match_surf)
v2.write_file("matches-v23.stl", r_surf)
