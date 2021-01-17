import DHLib

if __name__ == '__main__':
    dh = DHLib.DHLib()

    """
    Simple example of Diffie Hellman encryption method.
    """

    # init private
    Alice_a = 51812512512512532643623263264
    Bob_b = 95217125125521236436243264364

    # init public p
    Alice_p = 8521251251251215626432343624
    Bob_p = Alice_p

    # init public g
    Bob_g = 12972511255121261261261251
    Alice_g = Bob_g

    # create public A, B
    Alice_AA = dh.encrypt(Alice_g, Alice_a, Alice_p)
    Bob_BB = dh.encrypt(Bob_g, Bob_b, Bob_p)

    # create general private K values
    Alice_K = dh.encrypt(Bob_BB, Alice_a, Alice_p)
    Bob_K = dh.encrypt(Alice_AA, Bob_b, Bob_p)

    print("General value[Alice_K]: ", Alice_K)
    print("General value[Bob_K]: ", Bob_K)
