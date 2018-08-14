def is_inside(point,rectangle):
    if point[0] < rectangle[0]:
        return False
    elif point[1] < rectangle[1]:
        return False
    elif point[0] > rectangle[0] + rectangle[2]:
        return False
    elif point[1] > rectangle[1] + rectangle[3]:
        return False
    else:
        return True