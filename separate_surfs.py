

def get_single_surf(filename, dbname):
    """From an isovolume meshset, separate out each separate surface.
    """
    mb = core.Core()
    mb.load_file(filename)
    root_set = mb.get_root_set()
    all_verts = mb.get_entities_by_type(root_set, types.MBVERTEX)
    i = 0
    while len(all_verts) > 0:

        # get full set of connected verts starting from a seed
        verts = [all_verts[0]]
        while True:
            vtmp = mb.get_adjacencies(mb.get_adjacencies(verts, 2, op_type=1), 0, op_type=1)
            if set(list(vtmp)) == set(list(verts)):
                break
            else:
                verts = vtmp

        # get the connected set of triangles that make the single surf
        tris = mb.get_adjacencies(verts, 2, op_type=1)
        surf = mb.create_meshset()
        mb.add_entities(surf, tris)

        # write to file
        r_surf = Range(surf)
        mb.write_file("{}-{}.vtk".format(dbname, i), r_surf)

        # remove surface from meshset
        mb.delete_entities(tris)
        mb.delete_entities(verts)

        # resassign vertices
        all_verts = mb.get_entities_by_type(root_set, types.MBVERTEX)
        i += 1


def main():
    get_single_surf("/home/kkiesling/Pokeball/Documents/CNERG/ww-files/ww-test-geoms/levels-assigned/3.stl", "3")
    #get_single_surf("/home/kkiesling/Pokeball/Documents/CNERG/ww-files/ww-test-geoms/levels-assigned/4.stl", "4")
    #get_single_surf("/home/kkiesling/Pokeball/Documents/CNERG/ww-files/ww-test-geoms/levels-assigned/5.stl", "5")



if __name__ == '__main__':
    main()
