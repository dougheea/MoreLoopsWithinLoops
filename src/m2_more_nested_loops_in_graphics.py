"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Emily Dougherty.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    height = rectangle.get_height()
    width = rectangle.get_width()
    center = rectangle.get_center()
    rectangle.attach_to(window)
    window.render()

    num_of_rect = 2
    for k in range(n - 1):
        for j in range(num_of_rect):
            upper_left = rg.Point(center.x - width * (num_of_rect)/2,
                                  center.y - (k+1) *
                                  height - height/2)
            lower_right = rg.Point(upper_left.x + width, upper_left.y + height)
            new_rect = rg.Rectangle(upper_left, lower_right)
            new_rect.attach_to(window)
            window.render()

            corner_1 = rg.Point(upper_left.x + j*width, upper_left.y)
            corner_2 = rg.Point(lower_right.x + j*width, lower_right.y)
            new_new_rect = rg.Rectangle(corner_1, corner_2)
            new_new_rect.attach_to(window)
            window.render()
        num_of_rect = num_of_rect + 1



# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
