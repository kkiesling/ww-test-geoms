import vol as v

def main():
    geom1 = v.IsoVolumes('fng-ww-tags.vtk', 'ww_n')
    levels = [1.e-6, 8.706e-6, 7.579e-5, 6.598e-4, 5.743e-3, 0.05]
    geom1.assign_levels(levels)
    geom1.generate_volumes(dbname="levels-assigned")

if __name__ == '__main__':
    main()
