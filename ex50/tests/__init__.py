#include<stdio.h> 
2 #include<stdlib.h> 
3 #include<time.h> 
4 int main() 
5 { 
6     srand(time(NULL)); 
7     int i; 
8      
9     printf("Random Number 9 : "); 
10     for(i=0;i<9;i++) 
11     { 
12         printf("%d", rand() % 10); 
13     } 
14     printf("%d", rand() % 1+9); 
15      
16 } 
