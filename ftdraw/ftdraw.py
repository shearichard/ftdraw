'''
Draws diagrams to a PDF document.

The diagrams can be broadly described as 'boxes, linked
by lines, in which text is written'
'''
import math 
from enum import Enum

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.colors import tan, black, green, red
from reportlab.lib.units import inch

from ftutils import getoutputpath, id_generator, formatxy 


class BoxDiagramStyle(Enum):
    STRAIGHTUP = 1
    DIAGONAL = 2


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

def write_interior_text(rl_cnv, x, y):
    '''
    Writes text in a given location. Intended
    to be used to write text into the middle
    of where a rectangle will appear in the
    output
    '''

    textobject = rl_cnv.beginText()

    textobject.setTextOrigin(x, y)
    textobject.setFont('Helvetica', 10)
    rl_cnv.setFillColor(red)
    rl_cnv.setStrokeColor(red)
    textobject.textLine(formatxy(x,y))

    rl_cnv.drawText(textobject)

def draw_rect_sandbox_straightup(rl_cnv):
    

    bx_ht = 40
    bx_wd = bx_ht * 1.6
    max_x = 300 # 650
    max_y = 400 # 400
    idx_x = 0
    idx_y = 0
    lst_arr_bx = []
    print(f'''math.floor(bx_wd * 2.0) = {math.floor(bx_wd * 2.0)}''')
    for x in range(50, max_x, math.floor(bx_wd * 2.0)):
        print(f'''x={x}''')
        for y in range(50, max_y, math.floor(bx_ht * 1.2)):
            if idx_x == 0:
                print("x = ", x, ". y = ", y, ". bx_ht = ", bx_ht, ". bx_wd = ", bx_wd)
                rl_cnv.setFillGray(0.9)
                rl_cnv.setStrokeGray(0.75)
                rl_cnv.rect(x , y , bx_wd , bx_ht , stroke=1 , fill=1)
                write_interior_text(rl_cnv, (x + (bx_wd*0.3)), (y + bx_ht - (bx_ht*0.7)))
                lst_arr_bx.append({'x': x, 'y': y, 'bx_ht': bx_ht, 'bx_wd': bx_wd })
            idx_y += 1
        idx_x += 1

    import pprint
    pprint.pprint(lst_arr_bx)
    draw_arr_sandbox(rl_cnv, lst_arr_bx)

    return rl_cnv


def draw_rect_sandbox_diagonal(rl_cnv):
    raise NotImplementedError()


def draw_rect_sandbox(enum_diag_style):
    '''
    Outputs a grid of boxes and places some text 
    in the middle of each box

    The output document is hardcoded as A4 landscape.
    '''

    rl_cnv = canvas.Canvas(getoutputpath("txt_obj_test.pdf"), landscape(pagesize=A4))

    if enum_diag_style == BoxDiagramStyle.STRAIGHTUP:
        rl_cnv = draw_rect_sandbox_straightup(rl_cnv)
    elif enum_diag_style == BoxDiagramStyle.STRAIGHTUP:
        rl_cnv = draw_rect_sandbox_diagonal(rl_cnv)
    else:
        raise NotImplementedError()

    rl_cnv.showPage()
    rl_cnv.save()

def draw_arr_sandbox(rl_cnv, lst_arr_bx):
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
            link_boxes(rl_cnv, lst_arr_bx[idx-1], lst_arr_bx[idx])

def link_boxes(rl_cnv, start_bx, end_bx):
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

    rl_cnv.setStrokeGray(0.75)

    p = rl_cnv.beginPath()

    p.moveTo(start_x, start_y)
    p.lineTo(end_x, end_y)

    p.close()
    rl_cnv.drawPath(p)
    


def get_start_on_box(start_bx):
    '''
    Works out the x/y coordinates of
    the point which is halfway along
    the bottom line of the box
    '''

    out_y = start_bx['y'] + start_bx['bx_ht']
    out_x = start_bx['x'] + (0.5 * start_bx['bx_wd'])

    return out_x, out_y


def get_end_on_box(end_bx):
    '''
    Works out the x/y coordinates of
    the point which is halfway along
    the top line of the box
    '''

    out_y = end_bx['y']
    out_x = end_bx['x'] + (0.5 * end_bx['bx_wd'])

    return out_x, out_y


def main():

    width, height = landscape(A4) 
    print("Document Width : " + str(width))
    print("Document Height : " + str(height))
    draw_rect_sandbox(BoxDiagramStyle.STRAIGHTUP)

if __name__ == "__main__":
    main()

