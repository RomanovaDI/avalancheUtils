import sys
#sys.path.append(r'/home/romanovadi/cases/avalanche/preAndPostProcessing/readAsc')
#sys.path.append("~/cases/avalanche/preAndPostProcessing/setFieldsDict.py")
#sys.path.append("~/cases/avalanche/preAndPostProcessing/blockMeshDict.py")
import numpy as np
from scipy import interpolate
from operator import add
import math
import readAsc as ra
import setFieldsDict as sfd
import blockMeshDict as bmd

def main(argv):
	mapfile, regionfile, cellsize, dz, flowdepth, soildepth, areaheight = ra.readFileNames(argv)
#	map_name, region_map_name, cellsize, depthOfSnowCover, heightOfCalculationArea = ra.readFileNames(argv)
	slope = ra.asc(mapfile, regionfile)
	slope.am, slope.rg = ra.interpolateMap(slope.am, slope.rg, cellsize)
	#bmd.createBlockMeshDict(slope.am, height=heightOfCalculationArea)
	bmd.createBlockMeshDictInclined(slope.am, height=areaheight, dz=dz)
#	sfd.createSetFieldsFourPhasesRotated(slope.am, slope.rg, height=depthOfSnowCover)
#	sfd.createSetFieldsRotated(slope.am, slope.rg, height=depthOfSnowCover)
#	sfd.createSetFieldsFourPhasesOnlySoilRotated(slope.am, slope.rg, height=depthOfFlow, height_soil=depthOfSoilCover)
	sfd.createSetFieldsFourPhasesSoilRotated(slope.am, slope.rg, height = flowdepth, height_soil = soildepth)
#	sfd.createSetFieldsRotatedHeight(slope.am, slope.rg)
#	sfd.createSetFieldsRotatedStartFinish(slope.am, slope.rg, height=depthOfSnowCover)
#	sfd.createSetFields(slope.am, slope.rg, height=heightOfCalculationArea)
#	sfd.createTopoSetRotatedStartFinish(slope.am, slope.rg, height=heightOfCalculationArea)

if __name__== "__main__":
	main(sys.argv)
