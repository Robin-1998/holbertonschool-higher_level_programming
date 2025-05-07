#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    if len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
        print("{}: {}".format(len(sys.argv) - 1, sys.argv[1]))
    if len(sys.argv) >= 3:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))

# pour manipuler les arguments on fait import sys
# on utilise sys.arg pour manipuler les arguments
# dans la boucle on rajoute 1 car on commence à l'élément Hello et non
# directement sur le fichier
