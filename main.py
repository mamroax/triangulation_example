import matplotlib.pyplot as plt

"""Draws a line based on the three numbers of points in array"""
def draw_line(point_string, list_of_points):
    x = []
    y = []


try:
    x = []
    y = []
    points_f = open('points.txt', 'r')  # откроем файл с координатами
    triangles_f = open('triangles.txt', 'r')  # откроем файл с треугольниками
    l = [line.split(";") for line in points_f]
    triangles_list = [line.split() for line in triangles_f]
    print(l)
    print(triangles_list)
    for i in l:
        x.append(float(i[0]))
        y.append(float(i[1]))

    plt.scatter(x, y)
    # x1 = [1, 2, 3, 4, 5]
    # y1 = [0.99, 0.49, 0.35, 0.253, 0.18]
    # plt.errorbar(x1, y1)
    for j in range(len(l)):
        draw_line(triangles_list[j], l)

    plt.show()
except Exception:
    print('Something goes wrong..')
finally:
    points_f.close()  # закроем файл с координатами
    triangles_f.close()  # закроем файл с треугольниками
