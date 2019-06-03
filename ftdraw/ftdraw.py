import math 

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.colors import tan, black, green, red
from reportlab.lib.units import inch

from ftutils import getoutputpath, id_generator, formatxy 

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

def write_interior_text(c, x, y):

    textobject = c.beginText()

    textobject.setTextOrigin(x, y)
    textobject.setFont('Times-Roman', 10)
    textobject.setFillColor(red)
    textobject.textLine(formatxy(x,y))

    c.drawText(textobject)

def rect_demo():

    c = canvas.Canvas(getoutputpath("txt_obj_test.pdf"), landscape(pagesize=A4))
    ht = 40
    wd = ht / 1.6
    max_x = 300 # 650
    max_y = 200 # 400
    for x in range(50, max_x, math.floor(wd * 2.0)):
        for y in range(50, max_y, math.floor(ht * 1.2)):
            print("x = ", x, ". y = ", y, ". ht = ", ht, ". wd = ", wd)
            c.rect(x , y , ht , wd , stroke=1 , fill=0)
            write_interior_text(c, (x + (wd*0.3)), (y + ht - (ht*0.7)))

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
