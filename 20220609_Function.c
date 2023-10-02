#include <stdio.h>

// Funktion wird erst später im Code erstellt
void meow(int n);

//Muss oben stehen, weil es Zeile für Zeile ausführt
int main(void)
{
   meow(3);   
}

void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meown\n");
    }
}
