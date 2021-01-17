from DHLib import Encrypt

if __name__ == '__main__':
    enc = Encrypt()
    """
    Simple example of Diffie Hellman encryption method.
    """

    one_byte: int = 2 ** (256 * 8)

    # init private
    Alice_a = one_byte * 134512125512  # be cool and use random values
    Bob_b = one_byte * 512581052108  # be cool and use random values

    # init public p
    Alice_p = one_byte * 85125125125  # be cool and use random values
    Bob_p = Alice_p

    # init public g
    Bob_g = one_byte * 120521512551  # be cool and use random values
    Alice_g = Bob_g

    # create public A, B
    Alice_AA = enc.do(Alice_g, Alice_a, Alice_p)
    Bob_BB = enc.do(Bob_g, Bob_b, Bob_p)

    # create general private K values
    Alice_K = enc.do(Bob_BB, Alice_a, Alice_p)
    Bob_K = enc.do(Alice_AA, Bob_b, Bob_p)

    print("\r\nGeneral value[ Alice_K ]: ", Alice_K)
    print("\r\nGeneral value[  Bob_K  ]: ", Bob_K)
    print("\r\nAre the values the same:  ", Alice_K == Bob_K)