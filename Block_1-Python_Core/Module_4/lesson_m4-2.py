import math

RADIUS_EARTH: float = 6371.01


def distance_between_cities(lat1: float, lon1: float, lat2: float = 51.5072, lon2: float = -0.1275) -> float:
    def calculate_distance():
        nonlocal lat1, lon1, lat2, lon2
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)

        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)
        result = RADIUS_EARTH * math.acos(
            math.sin(lat1) * math.sin(lat2)
            + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)
        )
        return result

    distance: float = calculate_distance()
    return distance


if __name__ == '__main__':
    print(distance_between_cities(lon1=30.523, lat1=50.45))


count: int = 0


def foo():
    global count
    count += 1


def baz():
    global count
    count += 1


baz()
foo()
print(count)

def modeling(factor, *_, correction=0.5):
    return factor * correction


print(modeling(4, 5, 6, correction=1.5))

def our_pow(base, exp):
    """
     :param base: base of degree
     :param exp: exponent must be greater than or equal to zero
     :return: base ** exp result
    """
    # print(base, exp)
    if exp <= 0:
        return 1
    if exp == 1:
        return base
    return base * our_pow(base, exp - 1)


print(__name__)

if __name__ == '__main__':
    print(our_pow(2, 3))
    help(our_pow)
    print(our_pow.__doc__)
    #  2 * 2 * 2

def amount_payment(payment):
    sum = 0
    for i in payment:
        if i > 0:
            sum += i
    return sum


payment = [1, 2, 3]



def prepare_data(data):
    new_data = sorted(data)
    for i in new_data:
        if i == max(new_data):
            new_data.remove(i)
        if i == min(new_data):
            new_data.remove(i)
    return new_data


data = [1, 2, 3]
