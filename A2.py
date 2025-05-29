def rect(l, b):
    area = l * b
    print(f"Area of rectangle is {area}")

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
rect(l, b)

def tri(b, h):
    area = (b * h) / 2
    print(f"Area of triangle is {area}")

b = int(input("Enter breadth for triangle: "))
h = int(input("Enter height: "))
tri(b, h)

def circle(r):
    area = 3.14 * r * r
    print(f"Area of circle is {area}")

r = int(input("Enter radius: "))
circle(r)

def square(s):
    area = s * s
    print(f"Area of square is {area}")

s = float(input("Enter side length: "))
square(s)
