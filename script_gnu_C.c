#include <stdio.h>
#include <stdlib.h>

void plotQuadratic(int a, int b, int c) {
    FILE *gnuplotPipe = popen("gnuplot -persistent", "w");
    if (!gnuplotPipe) {
        fprintf(stderr, "Erro ao abrir o pipe do Gnuplot\n");
        exit(1);
    }

    fprintf(gnuplotPipe, "set xlabel 'x'\n");
    fprintf(gnuplotPipe, "set ylabel 'f(x)'\n");
    fprintf(gnuplotPipe, "set title 'Gráfico da Função Quadrática'\n");
    fprintf(gnuplotPipe, "set grid\n");
    fprintf(gnuplotPipe, "set xrange [-10:10]\n");
    fprintf(gnuplotPipe, "set yrange [-100:100]\n");

    // Aqui os valores inteiros são passados sem problemas
    fprintf(gnuplotPipe, "plot %d*x**2 + %d*x + %d with lines title 'f(x) = %dx^2 + %dx + %d'\n",
            a, b, c, a, b, c);

    pclose(gnuplotPipe);
}

int main() {
    int a, b, c;
    
    printf("Informe os coeficientes inteiros da equação quadrática (a, b, c): ");
    scanf("%d %d %d", &a, &b, &c);

    plotQuadratic(a, b, c);

    return 0;
}

