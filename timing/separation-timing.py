from pymoab import core, types
from pymoab.rng import Range
import time

def separate(fpath):
    # start pymoab instance
    mb = core.Core()

    # load file and get set of all verts
    mb.load_file(fpath)
    root_set = mb.get_root_set()
    all_verts = mb.get_entities_by_type(root_set, types.MBVERTEX)

    i = 0
    start_length = len(all_verts)

    while len(all_verts) > 0:

        # get full set of connected verts starting from a seed
        verts = [all_verts[0]]
        start = time.time()
        while True:
            # this step takes too long for large surfaces
            vtmp = mb.get_adjacencies(mb.get_adjacencies(verts, 2, op_type=1), 0, op_type=1)
            if len(vtmp) == len(verts):
                end = time.time()
                break
            else:
                verts = vtmp

        print("{}    {}".format(len(verts), end-start))

        # get the connected set of triangles that make the single surf
        tris = mb.get_adjacencies(verts, 2, op_type=1)
        surf = mb.create_meshset()
        mb.add_entities(surf, tris)

        # remove surface from meshset
        mb.delete_entities(tris)
        mb.delete_entities(verts)

        # resassign vertices
        all_verts = mb.get_entities_by_type(root_set, types.MBVERTEX)
        i += 1


if __name__ == '__main__':
    separate("./multi-surfs.stl")
