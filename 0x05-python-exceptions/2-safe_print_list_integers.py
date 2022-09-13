#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while (i in range(x)):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
            i += 1
        except (TypeError, ValueError):
            i += 1
        except IndexError:
            raise
    print()
    return(count)
