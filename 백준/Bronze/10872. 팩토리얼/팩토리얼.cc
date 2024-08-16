#include <stdio.h>
int fac(int n)
{
	if(n>0)
		return n*fac(n-1);
	else
		return 1;
}

int main()
{
	int n;
	scanf("%d",&n);
	int res=fac(n);
	printf("%d",res);
}