import numpy
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
ax =plt.axes(projection='3d')

def plotPoseSpline(ax, poseSpline, dt=0.1, invert=False, linespec='b-'):
    # generate a 3d curve.
    curve = []
    if invert:
        curve = numpy.array([ poseSpline.inverseTransformation(t)[0:3,3] for t in numpy.append(numpy.arange(poseSpline.t_min(),poseSpline.t_max(),dt),poseSpline.t_max())])
    else:
        curve = numpy.array([ poseSpline.position(t) for t in numpy.append(numpy.arange(poseSpline.t_min(),poseSpline.t_max(),dt),poseSpline.t_max())])
    #print "plotting the 3d curves"
    #ax.plot3D(curve[:,0], curve[:,1], curve[:,2],linespec)
    print "printing pose splines to file txt files\n"
    #print curve
    f = open("X-coords.txt","w")
    f.write(str(curve[:,0]))
    f.close()

    f = open("Y-coords.txt","w")
    f.write(str(curve[:,1]))
    f.close()

    f = open("Z-coords.txt", "w")
    f.write(str(curve[0:,2]))
    f.close()
