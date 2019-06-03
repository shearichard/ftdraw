from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.colors import tan, black, green, red
from reportlab.lib.units import inch

from ftutils import getoutputpath 

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

def textobject_demo():
    my_canvas = canvas.Canvas(getoutputpath("txt_obj_test.pdf"), landscape(pagesize=A4))
    # Create textobject
    textobject = my_canvas.beginText()
    #
    if False:
        import pprint
        pprint.pprint(dir(textobject))
    #
    # Set text location (x, y)
    textobject.setTextOrigin(10, 730)
    # Set font face and size
    textobject.setFont('Times-Roman', 12)
    # Write a line of text + carriage return
    textobject.textLine(text='Python rocks!')
    # Change text color
    textobject.setFillColor(red)
    # Write red text
    textobject.textLine(text='Python rocks in red!')
    # Write text to the canvas
    my_canvas.drawText(textobject)
    my_canvas.save()

def rect_demo():
    c = canvas.Canvas(getoutputpath("txt_obj_test.pdf"), landscape(pagesize=A4))
    ht = 75
    wd = 75
    for y in [100, 200, 300, 400]:
        for x in [100, 200, 300, 400, 500, 600]:
            c.rect(x , y , ht , wd , stroke=1 , fill=0)

    c.showPage()
    c.save()

def main():
    if False:
        c = canvas.Canvas(getoutputpath('myfile0.pdf'), pagesize=landscape(A4))
        c.setStrokeColor(green)
        width, height = landscape(A4) 
        hello(c)
        star(c, "Sirius", "a start", 200, 200, 5);
        ###########################
        u = inch/10
        c.setFillColor(tan)
        c.rect(10*u,0,20*u,10*u, stroke=1, fill=1)
        c.setFillColor(black)
        c.rect(23*u,0,8*u,10*u,fill=1)
        ###########################
        c.showPage()
        c.showPage()
        c.save()
        #
        create_form("formexample.pdf", "3-6-2019", "20.00", "Fred")
    #
    width, height = landscape(A4) 
    print("Width: " + str(width))
    print("Height: " + str(height))
    textobject_demo()
    rect_demo()

if __name__ == "__main__":
    main()
