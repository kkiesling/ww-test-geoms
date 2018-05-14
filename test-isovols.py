import vol as v

def main():
    g = v.IsoVolumes('fng-ww-tags.vtk', 'ww_n')
    #levels = [1.e-6, 8.706e-6, 7.579e-5, 6.598e-4, 5.743e-3, 0.05]
    levels = [6.598e-4, 5.743e-3, 0.05]
    g.assign_levels(levels)
    g.create_geometry()
    #geom1.generate_volumes()
    #geom1.generate_contours()
    #geom1.separate_surfs()

if __name__ == '__main__':
    main()
