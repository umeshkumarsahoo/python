import math
def calc(height,width):
    area=height*width
    no=math.ceil(area/5)
    return no

test_h=int(input("what is height of the wall: "))
test_b=int(input("what is the width of wall: "))
print(f"number of paints required to paint the wall is {calc(test_h,test_b)}")

