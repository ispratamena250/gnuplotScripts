#Script para gerar todos os monômios para a generalização x^k + y^k = 0 com (k = 0, 1, 2, 3)
import subprocess

def main():
    arr = [None] * 16 #titles
    count = 1

    with open("monomios.dat", "w") as file:
        for i in range(1, 5):
            for j in range(1, 5):
                aux = f"f{count}(x) = (-x)**({i}/{j}), /\ \n"
                file.write(aux)
                arr[count-1] = f"f{count}(x) = (-x)^({i}/{j})"
                aux = f"g{count}(x) = -((-x)**({i}/{j})), /\ \n"
                file.write(aux)
                arr[count] = f"g{count}(x) = ((-x)^({i}/{j}))"
                count += 1

                if count >= 16:
                    for k in range(16):
                        aux = f'f{count}(x) w l lw 4 t "{arr[k]}"\n'
                        file.write(aux)
                        aux = f'g{count}(x) w l lw 4 t "{arr[k+1]}"\n'
                        file.write(aux)

    file.close()

    subprocess.run(["xdg-open", "monomios.dat"])

if __name__ == "__main__":
    main()
