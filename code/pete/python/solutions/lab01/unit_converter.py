def converter(from_unit, to_unit, distance):
    """Given a from_unit ('mi', 'm', 'km', 'ft'),
    a to_unit ('mi', 'm', 'km', 'ft'), and a distance (int/float),
    returns a value of distance converter from from_unit to to_unit"""

    to_meters = {
        'ft': 0.3048,
        'mi': 1609.34,
        'm': 1,
        'km': 1000,
    }

    from_meters = {
        'ft': 1 / 0.3048,
        'mi': 1 / 1609.34,
        'm': 1 / 1,
        'km': 1 / 1000,
    }

    distance_in_meters = distance * to_meters[from_unit]
    result = distance_in_meters * from_meters[to_unit]

    return round(result, 1)