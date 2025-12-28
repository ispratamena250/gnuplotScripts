#RGB scale
def main():
    out = 0

    while(True):
        if out == 0:
            count = 255
            print("Red: ")
            for i in range(8):
                print(f"#{count:02X}0000")
                count -= 32

        if out == 1:
            count = 255
            print("Green: ")
            for i in range(8):
                print(f"#00{count:02X}00")
                count -= 32

        if out == 2:
            count = 255
            print("Blue: ")
            for i in range(8):
                print(f"#0000{count:02X}")
                count -= 32

        out += 1
        if out >= 3:
            break


if __name__ == "__main__":
    main()

    print()
