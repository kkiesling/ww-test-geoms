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
v2.load_file("./tmp/vols/0.stl")
v2r = v2.get_root_set()
v2_all_verts = v2.get_entities_by_type(v2r, types.MBVERTEX)

v3 = core.Core()
v3.load_file("./tmp/vols/1.stl")
v3r = v3.get_root_set()
v3_all_verts = v3.get_entities_by_type(v3r, types.MBVERTEX)

v2_coords = {}
for v in v2_all_verts:
    v2_coords[v] = tuple(v2.get_coords(v))

v3_coords = {}
for v in v3_all_verts:
    v3_coords[v] = tuple(v3.get_coords(v))

match_eh2 = []
match_coords = []
diff_eh = []
#print(v3_coords.values())
for vert in v2_coords.items():
    #print(vert)
    eh = vert[0]
    coord = vert[1]
    #print(coord)

    if coord in v3_coords.values():
        match_eh2.append(eh)
        match_coords.append(coord)

match_eh3 = []
for vert in v3_coords.items():
    eh = vert[0]
    coord = vert[1]
    if coord in match_coords:
        match_eh3.append(eh)

#print(sorted(v2_coords.values()))
#print(sorted(v3_coords.values()))

# (1) create a meshset from match_eh2 (child_meshset)
# (2) delete match_eh2 from vol 2
# (3) delete match_eh3 from vol 3
# (4) add child_meshset as child to each vol 2 and vol 3

# get the connected set of triangles that make the single surf
# diff_tris = v2.get_adjacencies(diff_eh, 2, op_type=1)
# diff_surf = v2.create_meshset()
# v2.add_entities(diff_surf, diff_tris)
#
# # write to file
# r_surf = Range(diff_surf)
# v2.write_file("diffs-v23.stl", r_surf)

# get the connected set of triangles that make the single surf
match_tris = v2.get_adjacencies(match_eh2, 2, op_type=1)
match_surf = v2.create_meshset()
# add as child to each vol

# try making the list of verts_to_add differently?
verts_to_add = v2.get_adjacencies(match_eh2, 1, op_type=1)
v2.add_entities(match_surf, match_tris)
v2.add_entities(match_surf, verts_to_add)

# # write to file
r_surf = Range(match_surf)
v2.write_file("matches-v01.stl", r_surf)

new_verts = v2.get_entities_by_type(match_surf, types.MBVERTEX)
print(new_verts)
