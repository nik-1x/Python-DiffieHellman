class DHLib:
    """ Diffie Hellman library """

    def __init__(self):
        print("Init:", self.__doc__)

    def encrypt(self, g: int, a: int, p: int) -> int:
        c = 0
        f = 1
        y = bin(a)
        y = y[2:len(y)]
        g = g % p
        for i in range(0, len(y)):
            c *= 2
            f = (f * f) % p
            if y[i] == '1':
                c += 1
                f = (f * g) % p
        return f

