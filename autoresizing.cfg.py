# experimentally fitted for my version of iosevka on a 4K 2x screen
# horizontal criteria: tX letters don't touch each other
# vertical criteria: p-over-b don't touch each other
# + reasonable height fit for my panel height

SIZES_SCALE_1 = {  # glyph width to (size, x_offt, y_offt)
    #4.0:  ( 7.5, -0, -0),  # -0 yofft is too compact!
    #5.0:  ( 9.0, -0, -0),  # -0 yofft is too compact!
    6.0:  (11.0, -0, -0),  # -1 yofft is too compact
    7.0:  (12.5, -0, -1),  # -2 yofft is too compact
    8.0:  (16.0, -1, -0),  # -0 yofft is too compact!
    9.0:  (18.0, -1, -0),  # -1 yofft is too compact
    10.0: (19.5, -1, -1),  # -2 yofft is too compact
    11.0: (21.5, -1, -0),  # -1 yofft is too compact
    12.0: (23.0, -1, -1),  # -2 yofft is too compact
    13.0: (26.5, -2, -1),  # -2 yofft is too compact
    14.0: (28.5, -2, -0),  # -1 yofft is too compact
    15.0: (30.0, -2, -0),  # -2 yofft is too compact
    16.0: (31.5, -2, -1),  # -2 yofft is too compact
    17.0: (35.0, -3, -2),  # -3 yofft is too compact
    18.0: (37.0, -3, -0),  # -2 yofft is too compact
    19.0: (38.5, -3, -0),  # -2 yofft is too compact
    20.0: (40.5, -3, -2),  # -3 yofft is too compact
    21.0: (42.0, -3, -1),  # -4 yofft is too compact
    22.0: (44.0, -3, -1),  # -3 yofft is too compact
    23.0: (45.5, -3, -0),  # -3 yofft is too compact
    24.0: (48.0, -4, -0),  # -3 yofft is too compact
}

SIZES_SCALE_2 = {  # glyph width to (size, x_offt, y_offt)
    4.0:  ( 8.0, -0.5, -0.0),  # -0.5 yofft is too compact
    4.5:  ( 9.0, -0.5, -0.0),  # -0.5 yofft is too compact
    5.0:  (10.0, -1.0, -1.0),  # -1.5 yofft is too compact
    5.5:  (11.0, -1.0, -0.0),  # -0.5 yofft is too compact
    6.0:  (12.0, -1.0, -1.0),  # -1.5 yofft is too compact
    6.5:  (13.0, -1.0, -0.5),  # -1.0 yofft is too compact
    7.0:  (14.0, -1.0, -0.5),  # -1.0 yofft is too compact
    7.5:  (15.0, -1.0, -0.5),  # -1.0 yofft is too compact
    8.0:  (16.0, -1.5, -1.0),  # -1.5 yofft is too compact
    8.5:  (17.0, -1.5, -0.0),  # -0.5 yofft is too compact
    9.0:  (18.0, -1.5, -0.5),  # -1.0 yofft is too compact
    9.5:  (19.0, -1.5, -1.5),  # -2.0 yofft is too compact
    10.0: (20.0, -1.5, -0.5),  # -1.0 yofft is too compact
    10.5: (21.0, -1.5, -1.5),  # -2.0 yofft is too compact
    11.0: (22.0, -1.5, -0.5),  # -1.5 yofft is too compact
    11.5: (23.0, -2.0, -1.0),  # -1.5 yofft is too compact
    12.0: (24.0, -2.0, -0.5),  # -1.5 yofft is too compact
    12.5: (25.0, -2.0, -1.0),  # -2.0 yofft is too compact
    13.0: (26.0, -2.0, -1.0),  # -2.0 yofft is too compact
    13.5: (27.0, -2.0, -1.5),  # -2.0 yofft is too compact
    14.0: (28.0, -2.0, -1.5),  # -2.5 yofft is too compact
    14.5: (29.0, -2.5, -1.5),  # -2.0 yofft is too compact
    15.0: (30.0, -2.5, -1.5),  # -2.5 yofft is too compact
    15.5: (31.0, -2.5, -1.5),  # -2.5 yofft is too compact
    16.0: (32.0, -2.5, -1.0),  # -2.5 yofft is too compact
    16.5: (33.0, -2.5, -2.5),  # -3.0 yofft is too compact
    17.0: (34.0, -2.5, -2.0),  # -2.5 yofft is too compact
    17.5: (35.0, -3.0, -1.0),  # -3.0 yofft is too compact
    18.0: (36.0, -3.0, -0.5),  # -2.5 yofft is too compact
    18.5: (37.0, -3.0, -2.0),  # -3.5 yofft is too compact
    19.0: (38.0, -3.0, -1.0),  # -2.5 yofft is too compact
    19.5: (39.0, -3.0, -2.5),  # -3.5 yofft is too compact
    20.0: (40.0, -3.0, -1.5),  # -3.0 yofft is too compact
    20.5: (41.0, -3.0, -2.5),  # -3.5 yofft is too compact
    21.0: (42.0, -3.5, -1.0),  # -3.5 yofft is too compact
    21.5: (43.0, -3.5, -2.5),  # -4.0 yofft is too compact
    22.0: (44.0, -3.5, -0.5),  # -3.5 yofft is too compact
    22.5: (45.0, -3.5, -2.0),  # -3.0 yofft is too compact
    23.0: (46.0, -3.5, -3.5),  # -4.0 yofft is too compact
    23.5: (47.0, -3.5, -1.0),  # -3.0 yofft is too compact
    24.0: (48.0, -4.0, -2.5),  # -4.0 yofft is too compact
}


def font(width, unused_height, scale_factor):
    glyph_width = width / scale_factor / 80
    sizes = SIZES_SCALE_2 if scale_factor > 1 else SIZES_SCALE_1
    params = None
    for w, p in sizes.items():
        if glyph_width >= w or params is None:
            params = p
    size, x_offt, y_offt = params
    r = {'size': size,
         'offset': {'x': int(x_offt * scale_factor),
                    'y': int(y_offt * scale_factor)}}
    print(width, f'{glyph_width:.2f}', r)
    return r
