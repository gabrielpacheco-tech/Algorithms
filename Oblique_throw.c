# Oblique-throw
//Calculator that shows many variables of an Oblique Throw (physics 1 subject)

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

  int main (void){
    float angulo, altura_inicial, velocidade, v0y, v0x, vy, vx, vf;
	float altura_atingida, alcance, tempo_de_subida, tempo_de_descida, tempo_total;  
    float g = 9.81;

    printf("Qual o angulo de lancamento? (em graus) \n");
    scanf("%f", &angulo);
    double angulo_radianos = angulo * M_PI / 180.0; // Conversão para radianos
    printf("Qual o modulo do vetor velocidade do lancamento? (em metros por segundo) \n");
    scanf("%f", &velocidade);
	printf("Qual a altura inicial do lancamento? (em metros) (Saber se o projeto foi lancado no nivel do solo) \n");
    scanf("%f", &altura_inicial);	
	 
	/* I will try to translate some portuguese terms to English lol (I am Brazillian)
 		
 Let's separate the motion in two components (vertically (y) and horizontally (x)) 	
		Vertically (y):
		
		v0y = velocidade(throw speed)*sin(angle);
		Going up:
		
			a = -g = -9.81 m/s^2, v0 = v0y, v = 0 m/s
			altura_atingida(max height) (delta y) = [(v^2 - (v0y^2) )/(2*a)] + altura_inicial(initial height);
			tempo_de_subida(going up time) = v0y/g;  
			                                 
		Free fall: a = g = +9.81 m/s^2, v0 = 0 m/s, altura = delta y = altura_atingida, v = ??
			tempo_de_descida (going down time) = tempo_de_subida
			tempo_total = tempo_de_subida + tempo_de_descida
			velocidade(componente y) final antes de atingir o solo = vy = sqrt((2*g*altura_atingida)
		
		Horizontally (x): v = v0 = const = velocidade, a = 0 m/s^2
	
			v0x = velocidade*cos(angulo)
			alcance = v0x*tempo_total
			velocidade(componente x) final antes de atingir o solo = vx = v0x
	*/
	  
	v0y = velocidade*sin(angulo_radianos);
	altura_atingida = ((v0y*v0y) / (2*g)) + altura_inicial;
	tempo_de_subida = v0y/g;
		if(altura_inicial == 0){
			tempo_de_descida = tempo_de_subida;
		}
		else{
			tempo_de_descida = sqrt(altura_atingida / (g/2));
		}
	tempo_total = tempo_de_subida + tempo_de_descida;
	 
	v0x = velocidade*cos(angulo_radianos);
	alcance = v0x*tempo_total;
	vy = sqrt(2*g*altura_atingida);
	vx = v0x;
	vf = sqrt(vx*vx + vy*vy);
	
	printf("v0y =  %.2f metros por segundo\n", v0y);
	printf("v0x =  %.2f metros por segundo\n", v0x);
	printf("Altura max atingida (delta Y): %.2f metros\n", altura_atingida);
	printf("Tempo de subida do projetil: %.2f segundos\n", tempo_de_subida);
	printf("Tempo de descida do projetil: %.2f segundos\n", tempo_de_descida);
	printf("Tempo total do projetil no ar: %.2f segundos\n", tempo_total);
	printf("Alcance (delta X): %.2f metros\n", alcance);
	printf("Componente y da velocidade max antes de atingir o solo: %.2f metros por segundo\n", vy);
	printf("Componente x da velocidade max antes de atingir o solo: %.2f metros por segundo\n", vx);
	printf("Modulo da velocidade max antes de atingir o solo: %.2f metros por segundo\n", vf);
	  
	  return 0;
  }
