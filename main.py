from DHLib import Encrypt

if __name__ == '__main__':
    enc = Encrypt()
    """
    Simple example of Diffie Hellman encryption method.
    """

    # init private
    Alice_a = 2**(256*8)*9
    Bob_b = 2**(256*8)*3

    # init public p
    Alice_p = 2**(256*8)*10
    Bob_p = Alice_p

    # init public g
    Bob_g = 2**(256*8)*3
    Alice_g = Bob_g

    # create public A, B
    Alice_AA = enc.do(Alice_g, Alice_a, Alice_p)
    Bob_BB = enc.do(Bob_g, Bob_b, Bob_p)

    # create general private K values
    Alice_K = enc.do(Bob_BB, Alice_a, Alice_p)
    Bob_K = enc.do(Alice_AA, Bob_b, Bob_p)

    print("General value[Alice_K]: ", Alice_K)
    print("General value[Bob_K]: ", Bob_K)
