#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	srand(time(NULL));
	FILE *file1 = fopen("dados1.dat", "w");
	if(!file1){
		printf("Error on file1\n");
		exit(1);
	}

	for(int i=0; i<100; i++){
		int x, y, z;
		x = rand() % 100;
		y = rand() % 100;
		z = rand() % 100;
		fprintf(file1, "%d\t%d\t%d\n", x, y, z);
	}

	fclose(file1);

	return 0;
}
