#include <stdio.h>
int main(){
	int input,i,A,B,input2,input3; 
	scanf("%d", &input); 
	if(input>=10){ 
		A = input/10; 
		B = input%10;  
		input2 = (A+B)%10; 
		input3 = (B*10)+input2; 
		i++; 
	}
	else{
		A = 0;
		B = input; 
		input3 = (input*10)+input;
		i++;
	}
	while(input3 != input){ 
		if(input3>=10){  
			A = input3/10;
			B = input3%10;
			input2 = (A+B)%10;
			input3 = (B*10)+input2;
			i++;
		}
		else{
			A = 0;
			B = input3; 
			input3 = (B*10)+B;
			i++;
		}
	}
	printf("%d",i); 
}