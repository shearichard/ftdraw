'''
A module of utilty functions for the 
ftdraw project.

The primary purpose of this module is to
to 'de-clutter' the primary module
'''

from datetime import datetime
import os
import string
import random
import math

RELATIVEPATHTOOUTPUT = '''../ftoutput'''

def timestampfilename(fname):
    '''
    Given a file name, such as 'a.txt' a time
    stamped version of the name is returned such
    as this 'a-20120115T143929.txt'
    '''
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
    '''
    Takes the file name provided in the `fname` argument,
    embeds a timestamp within it and creates a path for
    that file name to the standard output directory
    '''
    fnamestamped = timestampfilename(fname)
    return os.path.join(RELATIVEPATHTOOUTPUT, fnamestamped)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    '''
    Produces a random string of, by default, uppercase letters and digits
    '''
    return ''.join(random.choice(chars) for _ in range(size))

def formatxy(x, y):
    '''
    Produces a string intended to display a rounded version
    of an x and y coordinate like this `100/200` where x 
    is 100 and y is 200
    '''
    return '{:d}/{:d}'.format(math.floor(x), math.floor(y))

############################################################################################   
############################################################################################   
############################################################################################   
############################################################################################   
############################################################################################   
############################################################################################   
############################################################################################   
def hello(c):
    c.drawString(100,100,"Hello World")

def star(canvas, title="Title Here", aka="Comment here.", xcenter=None, ycenter=None, nvertices=5):

    from math import pi
    from reportlab.lib.units import inch

    radius=inch/3.0

    if xcenter is None: 
        xcenter=2.75*inch
    if ycenter is None: 
        ycenter=1.5*inch

    canvas.drawCentredString(xcenter, ycenter+1.3*radius, title)
    canvas.drawCentredString(xcenter, ycenter-1.4*radius, aka)
    p = canvas.beginPath()
    p.moveTo(xcenter,ycenter+radius)

    #canvas.strokeColor(green)

    from math import pi, cos, sin

    angle = (2*pi)*2/5.0
    startangle = pi/2.0
    
    for vertex in range(nvertices-1):
        nextangle = angle*(vertex+1)+startangle
        x = xcenter + radius*cos(nextangle)
        y = ycenter + radius*sin(nextangle)
        p.lineTo(x,y)
        
    if nvertices==5:
        p.close()

    canvas.drawPath(p)
    
def create_form(filename, date, amount, receiver):
    """
    @param date: The date to use
    @param amount: The amount owed
    @param receiver: The person who received the amount owed
    """
    form_canvas = canvas.Canvas(getoutputpath(filename), pagesize=A4)
    form_canvas.setLineWidth(.3)
    form_canvas.setFont('Helvetica', 12)
    form_canvas.drawString(30, 750,'OFFICIAL COMMUNIQUE')
    form_canvas.drawString(30, 735,'OF ACME INDUSTRIES')
    form_canvas.drawString(500, 750, date)
    form_canvas.line(480, 747, 580, 747)
    form_canvas.drawString(275, 725,'AMOUNT OWED:')
    form_canvas.drawString(500, 725, amount)
    form_canvas.line(378,723, 580, 723)
    form_canvas.drawString(30, 703,'RECEIVED BY:')
    form_canvas.line(120, 700, 580, 700)
    form_canvas.drawString(120, 703, receiver)
    form_canvas.save()


