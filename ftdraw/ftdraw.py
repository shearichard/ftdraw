import math 

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.colors import tan, black, green, red
from reportlab.lib.units import inch

from ftutils import getoutputpath 

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
    wd = 75 / 1.6
    for x in range(50, 600, math.floor(wd * 2.0)):
        for y in range(50, 500, math.floor(ht * 1.6)):
            print("x = ", x, ". y = ", y)
            c.rect(x , y , ht , wd , stroke=1 , fill=0)

    c.showPage()
    c.save()

def main():

    width, height = landscape(A4) 
    print("Width: " + str(width))
    print("Height: " + str(height))
    textobject_demo()
    rect_demo()

if __name__ == "__main__":
    main()
