from datetime import datetime
import os

RELATIVEPATHTOOUTPUT = '''../ftoutput'''

def timestampfilename(fname):
    d=datetime.now()
    isonow = d.strftime('%Y%m%dT%H%M%S') #'outputs something like : 20120115T143929'
    #
    arr_fname_in = fname.split(".")
    #
    arr_fname_out = arr_fname_in[:1]
    arr_fname_out.extend(["-" + isonow + "."])
    arr_fname_out.extend(arr_fname_in[-1])
    #
    fn_stamped = "".join(arr_fname_out)
    #
    return fn_stamped

def getoutputpath(fname):
    fnamestamped = timestampfilename(fname)
    return os.path.join(RELATIVEPATHTOOUTPUT, fnamestamped)

