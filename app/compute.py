from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob

def damped_vibrations(t, A, b, w):
    return A*exp(-b*t)*cos(w*t)

def compute(A, b, w, T, resolution=500):
    """Return the filename of the plot of the damped vibration function"""
    t = linspace(0, T,resolution)
    u=damped_vibrations(t, A, b, w)
    plt.figure()
    plt.plot(t,u)
    plt.title("A=%g, b=%g, w=%g" %(A,b,w))
    mypath = os.path.dirname(os.path.abspath(__file__))+'/static/'
    if not os.path.isdir(mypath):
         os.mkdir(mypath)
    else:
         for filename in glob.glob(os.path.join(mypath,'*.png')):
            #  print "I am in file removal"
            #  print "filename: %r" %(filename)
             os.remove(filename)
    mypath = os.path.dirname(os.path.abspath(__file__))+'/static/'
    fname = str(time.time())+'.png'
    plotfile=os.path.join(mypath, fname)
    plt.savefig(plotfile)
    reqpath = '../static/' + fname
    return reqpath

def compute_nofile(A,b,w,T,resolution=500):
    t = linspace(0,T,resolution+1)
    u = damped_vibrations(t, A, b, w)
    plt.figure()
    plt.plot(t,u)
    plt.title("A=%g, b=%g, w=%g" %(A,b,w))

    from io import BytesIO
    figfile=BytesIO()
    plt.savefig(figfile,format='png')
    figfile.seek(0)
    import base64
    figdata_png = base64.b64encode(figfile.getvalue())
    return figdata_png

def compute_svg(A,b,w,T,resolution=500):
    t = linspace(0,T,resolution+1)
    u = damped_vibrations(t, A, b, w)
    plt.figure()
    plt.plot(t,u)
    plt.title("A=%g, b=%g, w=%g" %(A,b,w))

    from io import BytesIO
    figfile=BytesIO()
    plt.savefig(figfile,format='svg')
    figfile.seek(0)
    figdata_svg='<svg' +figfile.getvalue().split('<svg')[1]
    figdata_svg = unicode(figdata_svg, 'utf-8')
    return figdata_svg
