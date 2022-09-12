import matplotlib.pyplot as plt


def draw_line(point_string:  list[list[str]], list_of_points:  list[list[str]]) -> plt:
    """Draws a line based on the three numbers of points in array"""
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

    # print(point1, point2, point3)
    # print(list_of_points[point1])
    plt.errorbar(x, y)
