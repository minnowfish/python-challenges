def circle_area(r):
    area = (r**2)*3.14
    return(area)

def circle_circumference(r):
    circumference = 2*r*3.14
    return(circumference)

radius = float(input("Input the radius of the circle"))
area = round(circle_area(radius), 3)
circumference = round(circle_circumference(radius),3)

print(f"The area of the circle is {area} and the circumference of the circle is {circumference}")
