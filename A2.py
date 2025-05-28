def area_Rect(l, b):
    ar = l * b
    print(f"Area of a Rectangle is: {ar}")


def area_Square(s):
    ar = s * s
    print(f"Area of a Square is: {ar}")


def area_circle(r):
    ar = 3.14 * (r * r)
    print(f"Area of the Circle is {ar}")


def area_Triangle(b, h):
    ar = (b * h) / 2
    print(f"Area of the Triangle {ar}")


print("Reading argument for Rectangle")
l = float(input("Enter the length: "))
b = float(input("Enter the breath: "))
area_Rect(l, b)

print("Reading argument for Square")
s = float(input("Enter the sides in CMS: "))
area_Square(s)

print("Reading argument for Circle")
r = float(input("Enter the radius: "))
area_circle(r)

print("Reading argument for Triangle")
b = float(input("Enter the Base: "))
h = float(input("Enter the Height: "))
area_Triangle(b, h)
