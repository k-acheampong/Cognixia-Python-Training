r = 4
h = 100


def area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area


c_area = area_of_circle(r)
print("c_area:", c_area)


def volume_of_cylinder(base_area, height):
    volume = base_area * height
    return volume


c_volume = volume_of_cylinder(c_area, h)
print("c_volume:", c_volume)
