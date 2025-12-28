#Script para gerar todos os monômios para a generalização x^k + y^k = 0 com (k = 1, 2, 3, 4)
import subprocess

rgbScale = []

def main():
    positive = []
    negative = []
    plots = []
    count = 1

    rgb()    

    with open("monomios.dat", "w") as file:
        for i in range(1, 5):
            for j in range(1, 5):
                aux = f"f{count}(x) = (-x)**({j}/{i})"
                positive.append(aux)

                aux = f'        f{count}(x) w l lw 4 lc rgb "{rgbScale[count]}" t "y^{i} + x^{j} = 0", \\'
                plots.append(aux)

                aux = f"g{count}(x) = -((-x)**({j}/{i}))"
                negative.append(aux)

                aux = f'        g{count}(x) w l lw 4 lc rgb "{rgbScale[count+1]}" notitle, \\'
                plots.append(aux)

                count += 1

    print(count)
    with open("monomios.dat", "w") as file:
        for i in range(len(positive)):
            file.write(f"{positive[i]}\n")
            file.write(f"{negative[i]}\n")
            print(i, end=" ")

        for j in range(len(plots)):
            file.write(f"{plots[j]}\n")

    file.close()

    subprocess.run(["xdg-open", "monomios.dat"])

def rgb():
    out = 0

    while(True):
        if out == 0:
            count = 255
            #print("Red: ")
            for i in range(8):
                rgbScale.append(f"#{count:02X}0000")
                count -= 32

        if out == 1:
            count = 255
            #print("Green: ")
            for i in range(8):
                rgbScale.append(f"#00{count:02X}00")
                count -= 32

        if out == 2:
            count = 255
            #print("Blue: ")
            for i in range(8):
                rgbScale.append(f"#0000{count:02X}")
                count -= 32

        out += 1
        if out >= 3:
            break

if __name__ == "__main__":
    main()

    print()
