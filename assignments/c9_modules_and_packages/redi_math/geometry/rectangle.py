def get_area(height, width):
    if height < 0 or width < 0:
        raise ValueError
    area = height * width
    return area
