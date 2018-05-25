'''this is the utility function file for term_start.py'''
# take in a float value and converts it to a cardinal direction string
# for use in determining direction of wind


def deg_to_dir(deg: int):
    if deg == 0 or deg == 360:
        return 'N'
    elif 1 <= deg <= 44:
        return 'NNE'
    elif deg == 45:
        return 'NE'
    elif 46 <= deg <= 89:
        return 'ENE'
    elif deg == 90:
        return 'E'
    elif 91 <= deg <= 134:
        return 'ESE'
    elif deg == 135:
        return 'SE'
    elif 136 <= deg <= 179:
        return 'SSE'
    elif deg == 180:
        return 'S'
    elif 181 <= deg <= 224:
        return 'SSW'
    elif deg == 225:
        return 'SW'
    elif 226 <= deg <= 269:
        return 'WSW'
    elif deg == 270:
        return 'W'
    elif 271 <= deg <= 314:
        return 'WNW'
    elif deg == 315:
        return 'NW'
    elif 316 <= deg <= 359:
        return 'NNW'
    else:
        return 'Error: not a coordinate'
