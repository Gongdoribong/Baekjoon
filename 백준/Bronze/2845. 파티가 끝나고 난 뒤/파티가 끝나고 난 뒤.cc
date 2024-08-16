#include <stdio.h>
int main()
{
	int a,b,c,d,e,L,P;
	scanf("%d %d",&L,&P);
	int yap=L*P;
	scanf("%d %d %d %d %d",&a,&b,&c,&d,&e);
	printf("%d %d %d %d %d",a-yap,b-yap,c-yap,d-yap,e-yap);
}