# Variables I will use often.
sep = "Xx--------------------Xx"
name = ""
print(sep)

# Name of player
while len(name) == 0:
    name = input("> Please enter your name: ")
    print(sep)

# Main menu
def sudoku():
    print("> Welcome to Sudoku!")
    print("1. Start Game\n"
          "2. Credits\n"
          "3. Quit Game")

    print(sep)
    opt = int(input("> "))

    while opt != 1 and opt != 2 and opt != 3:
        opt = int(input("> "))

    if opt == 1:
        import random

        # Shuffling numbers
        num = [1,2,3,4,5,6,7,8,9]
        random.shuffle(num)

        # Appending numbers
        a = num[0]
        b = num[1]
        c = num[2]
        d = num[3]
        e = num[4]
        f = num[5]
        g = num[6]
        h = num[7]
        i = num[8]

        print(sep)

# Answering the questions
        def part2():

            # Board Layout
            print(f"_ {b} _  _ {e} _  {g} _ {h}\n"
                  f"{d} _ {f}  _ _ {i}  _ _ {c}\n"
                  f"{g} _ {i}  {a} _ _  {d} _ _")
            print("")
            print(f"{c} _ {b}  _ _ {e}  {f} _ _\n"
                  f"{h} _ {d}  {f} _ _  {b} _ _\n"
                  f"_ {f} _  {b} {c} _  {h} _ _")
            print("")
            print(f"_ {d} _  {c} _ _  {i} _ {g}\n"
                  f"{f} _ {g}  {i} _ _  {e} _ _\n"
                  f"_ {a} _  {e} {d} _  {c} _ _")

            print(sep)

            print("> The options to answer go from left to right and up to down.\n"
                  "> If you type a wrong answer, you will lose a life.\n"
                  "> If you want to go back from any option, just press 0.\n"
                  "> Do not repeat the choices if you have already done them.")
            print(sep)
            ans = int(input("> Enter a value from 1-45: "))
            print(sep)

            while ans <= 0 and ans >= 46:
                ans = int(input("> Enter a value from 1-45: "))
                print(sep)

            if ans == 1:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == a:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    print(sep)
                    part2()

            if ans == 2:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == c:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    print(sep)
                    part2()

            if ans == 3:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == d:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    print(sep)
                    part2()

            if ans == 4:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == f:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    print(sep)
                    part2()

            if ans == 5:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == i:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    print(sep)
                    part2()

            if ans == 6:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == e:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    print(sep)
                    part2()

            if ans == 7:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == g:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    print(sep)
                    part2()

            if ans == 8:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == h:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    print(sep)
                    part2()

            if ans == 9:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == a:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    print(sep)
                    part2()

            if ans == 10:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == b:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 11:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == h:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 12:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == b:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 13:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == c:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 14:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == e:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 15:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == f:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 16:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == g:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 17:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == h:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 18:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == i:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 19:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == d:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 20:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == a:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 21:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == i:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 22:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == g:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 23:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == a:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 24:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == c:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 25:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == e:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 26:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == e:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 27:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)
                    part2()

                if dor == a:
                    print("> Your answer was correct!")
                    print(sep)
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 28:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == d:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 29:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == g:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 30:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == i:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 31:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == b:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 32:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == e:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 33:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == f:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 34:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == h:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 35:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == a:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 36:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == c:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 37:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == a:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 38:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == b:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 39:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == h:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 40:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == d:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 41:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == i:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 42:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == h:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 43:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == g:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 44:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == f:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()

            if ans == 45:
                dor = int(input("> Please enter your answer: "))
                print(sep)

                while dor < 0 and dor > 9:
                    dor = int(input("> Please enter your answer: "))
                    print(sep)

                if dor == b:
                    print("> Your answer was correct!")
                    print(sep)
                    part2()
                elif dor == 0:
                    part2()
                else:
                    print("> Wrong! Try Again!")
                    part2()


        part2()

# Credits
    elif opt == 2:
        print(sep)
        print("> This game is made by Mohan 9B and Erica 9B.")
        print("> Press 0 to return to the menu.")
        print(sep)
        option = int(input("> "))
        print(sep)

        while option != 0:
            option = int(input("> "))
            print(sep)

        if option == 0:
            sudoku()

# Quit
    elif opt == 3:
        quit()

sudoku()