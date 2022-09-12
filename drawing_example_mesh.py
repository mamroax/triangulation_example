import matplotlib.pyplot as plt
from triangulation_example.functions import draw_triangle

try:
    x = []
    y = []
    points_file = open('text_files/points.txt', 'r')  # откроем файл с координатами
    triangles_file = open('text_files/triangles.txt', 'r')  # откроем файл с треугольниками
    points_line = [line.split(";") for line in points_file]
    print('Длина массива координат ', len(points_line))
    triangles_list = [line.split() for line in triangles_file]
    print(points_line)
    print('Длина массива точек ', len(triangles_list))
    print(triangles_list)
    for i in points_line:
        x.append(float(i[0]))
        y.append(float(i[1]))

    plt.scatter(x, y)
    # x1 = [1, 2, 3, 4, 5]
    # y1 = [0.99, 0.49, 0.35, 0.253, 0.18]
    # plt.errorbar(x1, y1)
    for j in range(len(triangles_list)):
        draw_triangle(triangles_list[j], points_line)

    plt.show()
except Exception:
    print('Something goes wrong..')
finally:
    points_file.close()  # закроем файл с координатами
    triangles_file.close()  # закроем файл с треугольниками
