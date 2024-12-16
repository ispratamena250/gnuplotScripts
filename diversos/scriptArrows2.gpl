#Script de treino sobre a função de arrows no gnuplot

set xlabel "x"
set ylabel "f(x)"
#set xrange [0:10]
#set yrange [-20:10]
set arrow 1 from 3,-7 to 1.16,-9.2 head filled size 0.70,20,30 linecolor rgb 'red'
set label 1 "Mínimo local" at 3.2,-6.7 textcolor rgb 'black'
set title "Função de exemplo"

f(x) = (cos(3*abs(x)))/log(abs(x))

plot f(x) with lines lc rgb 'blue' title "f(x) = (cos(3x))/log(x)"
