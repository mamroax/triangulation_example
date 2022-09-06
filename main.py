import matplotlib.pyplot as plt

"""Draws a line based on the three numbers of points in array"""
def draw_line(point_string, list_of_points):
    point1 = int(point_string[0].split(';')[0])
    point2 = int(point_string[0].split(';')[1])
    point3 = int(point_string[0].split(';')[2])

    x = []
    y = []

    x.append(float(list_of_points[point1][0]))
    y.append(float(list_of_points[point1][1]))
    x.append(float(list_of_points[point2][0]))
    y.append(float(list_of_points[point2][1]))
    x.append(float(list_of_points[point3][0]))
    y.append(float(list_of_points[point3][1]))
    x.append(float(list_of_points[point1][0]))
    y.append(float(list_of_points[point1][1]))

    #print(point1, point2, point3)
    #print(list_of_points[point1])
    plt.errorbar(x, y)



try:
    x = []
    y = []
    points_f = open('points.txt', 'r')  # откроем файл с координатами
    triangles_f = open('triangles.txt', 'r')  # откроем файл с треугольниками
    l = [line.split(";") for line in points_f]
    print('Длина массива координат ', len(l))
    triangles_list = [line.split() for line in triangles_f]
    print(l)
    print('Длина массива точек ', len(triangles_list))
    print(triangles_list)
    for i in l:
        x.append(float(i[0]))
        y.append(float(i[1]))

    plt.scatter(x, y)
    # x1 = [1, 2, 3, 4, 5]
    # y1 = [0.99, 0.49, 0.35, 0.253, 0.18]
    # plt.errorbar(x1, y1)
    for j in range(len(triangles_list)):
        draw_line(triangles_list[j], l)

    plt.show()
except Exception:
    print('Something goes wrong..')
finally:
    points_f.close()  # закроем файл с координатами
    triangles_f.close()  # закроем файл с треугольниками
