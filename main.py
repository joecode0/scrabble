import time

import letter_to_word_dict as ltwd

if __name__ == '__main__':
    t1 = time.time()

    ltwd.EOWL_to_single_txt("EOWL/", "dictionary.txt")

    t2 = time.time()

    print("Time: {}".format(round(t2-t1, 2)))
