Symbol x,a;
CFunction den;
Local expr = den(1-2*x);
#define N "5"
splitarg (x) den;
repeat;
identify den(a?,x?) = 1/a - x/a * den(a,x);
if (count(x,1) > `N') discard;
endrepeat;
Print;
.end
