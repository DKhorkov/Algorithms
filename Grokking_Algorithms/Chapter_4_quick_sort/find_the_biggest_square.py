"""Задача найти разделить прямоугольник с заданной шириной и длинной на одинаковые квадраты
(нужно получить наибольшую возможную сторону квадрата)"""


def biggest_square_face(rect_length, rect_height):
    if rect_length == rect_height:
        return rect_length
    if rect_length > rect_height:
        return biggest_square_face(rect_height, rect_length - rect_height)
    else:
        return biggest_square_face(rect_length, rect_height - rect_length)


print(biggest_square_face(400, 120))
