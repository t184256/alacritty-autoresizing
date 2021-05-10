OFFT0 = {'offset': {'x': -2, 'y': -0}, 'glyph_offset': {'x': -1, 'y': -1}}
OFFT1 = {'offset': {'x': -2, 'y': -1}, 'glyph_offset': {'x': -1, 'y': -1}}
SIZES = {  # glyph width to font parameters mapping for my font
    6.00:  {'size': 14.0, **OFFT0},  # same width: 13.0-14.5
    7.00:  {'size': 15.5, **OFFT0},  # same width: 15.0-16.0
    8.00:  {'size': 17.0, **OFFT1},  # same width: 16.5-18.0
    9.00:  {'size': 18.5, **OFFT1},  # same width: 18.5-19.5
    10.00: {'size': 20.0, **OFFT1},  # same width: 20.0-21.5
    11.00: {'size': 22.5, **OFFT1},  # same width: 22.0-23.0
    12.00: {'size': 24.0, **OFFT1},  # same width: 23.5-25.0
    13.00: {'size': 25.5, **OFFT1},  # same width: 25.5-26.5
    14.00: {'size': 27.0, **OFFT1},  # same width: 27.0-28.0
    15.00: {'size': 29.5, **OFFT1},  # same width: 28.5-30.0
    16.00: {'size': 31.0, **OFFT1},  # same width: 30.5-31.5
    17.00: {'size': 32.5, **OFFT1},  # same width: 32.0-33.5
    18.00: {'size': 34.0, **OFFT1},  # same width: 34.0-35.0
    19.00: {'size': 36.5, **OFFT1},  # same width: 35.5-37.0
    20.00: {'size': 38.5, **OFFT1},  # same width: 37.5-38.5
    21.00: {'size': 40.0, **OFFT1},  # same width: 39.0-40.5
    22.00: {'size': 41.5, **OFFT1},  # same width: 41.0-42.0
    23.00: {'size': 43.0, **OFFT1},  # same width: 42.5-43.5
    24.00: {'size': 45.0, **OFFT1},  # same width: 44.0-45.5
    25.00: {'size': 46.5, **OFFT1},  # same width: 46.0-47.0
    26.00: {'size': 48.5, **OFFT1},  # same width: 47.5-49.0
    27.00: {'size': 50.0, **OFFT1},  # same width: 49.5-50.5
    28.00: {'size': 52.0, **OFFT1},  # same width: 51.0-52.5
    29.00: {'size': 53.5, **OFFT1},  # same width: 53.0-54.0
    30.00: {'size': 55.5, **OFFT1},  # same width: 54.5-56.0
    31.00: {'size': 57.0, **OFFT1},  # same width: 56.5-57.5
    32.00: {'size': 58.5, **OFFT1},  # same width: 58.0-59.0
}


def font(width, unused_height):
    params = None
    glyph_width = width / 80
    for w, p in SIZES.items():
        if glyph_width >= w or params is None:
            params = p
    print(width, glyph_width, params['size'])
    return params
