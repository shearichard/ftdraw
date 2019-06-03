'''
Draws diagrams to a PDF document.

The diagrams can be broadly described as 'boxes, linked
by lines, in which text is written'
'''
import math 

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.colors import tan, black, green, red
from reportlab.lib.units import inch

from ftutils import getoutputpath, id_generator, formatxy 

def textobject_demo():
    '''
    This is only here to demonstrate how a Docstring is done. It should
    be removed quite soon
    '''

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
    '''
    Writes text in a given location. Intended
    to be used to write text into the middle
    of where a rectangle will appear in the
    output
    '''

    textobject = c.beginText()

    textobject.setTextOrigin(x, y)
    textobject.setFont('Times-Roman', 10)
    textobject.setFillColor(red)
    textobject.textLine(formatxy(x,y))

    c.drawText(textobject)

def draw_rect_sandbox():
    '''
    Outputs a grid of boxes and places some text 
    in the middle of each box

    The output document is hardcoded as A4 landscape.
    '''

    c = canvas.Canvas(getoutputpath("txt_obj_test.pdf"), landscape(pagesize=A4))
    ht = 40
    wd = ht * 1.6
    max_x = 300 # 650
    max_y = 200 # 400
    idx_x = 0
    idx_y = 0
    lst_arr_bx = []
    for x in range(50, max_x, math.floor(wd * 2.0)):
        for y in range(50, max_y, math.floor(ht * 1.2)):
            if idx_x == 0:
                print("x = ", x, ". y = ", y, ". ht = ", ht, ". wd = ", wd)
                c.rect(x , y , wd , ht , stroke=1 , fill=0)
                write_interior_text(c, (x + (wd*0.3)), (y + ht - (ht*0.7)))
                lst_arr_bx.append({'x': x, 'y': y, 'ht': ht, 'wd': wd })
            idx_y += 1
        idx_x += 1

    import pprint
    pprint.pprint(lst_arr_bx)
    draw_arr_sandbox(c, lst_arr_bx)

    c.showPage()
    c.save()

def draw_arr_sandbox(c, lst_arr_bx):
    '''
    Draw lines linking each element of the
    argument `lst_arr_bx` so that a line
    joins 0-1, 1-2, 2-3 etc.
    '''
    idx = 0
    first_bx = True

    for idx in range(len(lst_arr_bx)):
        print(idx)
        if first_bx:
            first_bx = False
        else:
            link_boxes(c, lst_arr_bx[idx-1], lst_arr_bx[idx])

def link_boxes(c, start_bx, end_bx):
    '''
    Draws a line between the start box and the 
    end box

    An assumption is made that the first box
    is above the second box
    '''
    start_x, start_y = get_start_on_box(start_bx)
    end_x, end_y = get_end_on_box(end_bx)
    print("")
    print('{:d}/{:d} to {:d}/{:d} '.format(math.floor(start_x), math.floor(start_y), math.floor(end_x), math.floor(end_y)))

    p = c.beginPath()

    p.moveTo(start_x, start_y)
    p.lineTo(end_x, end_y)

    p.close()
    c.drawPath(p)
    


def get_start_on_box(start_bx):
    '''
    Works out the x/y coordinates of
    the point which is halfway along
    the bottom line of the box
    '''

    out_y = start_bx['y'] + start_bx['ht']
    out_x = start_bx['x'] + (0.5 * start_bx['wd'])

    return out_x, out_y


def get_end_on_box(end_bx):
    '''
    Works out the x/y coordinates of
    the point which is halfway along
    the top line of the box
    '''

    out_y = end_bx['y']
    out_x = end_bx['x'] + (0.5 * end_bx['wd'])

    return out_x, out_y


def main():

    width, height = landscape(A4) 
    print("Document Width : " + str(width))
    print("Document Height : " + str(height))
    draw_rect_sandbox()

if __name__ == "__main__":
    main()
