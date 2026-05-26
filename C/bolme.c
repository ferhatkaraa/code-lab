#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int bol(int bolunen, int bolen) {
        int bolum=0;
        int kalan;
        for (int i = 0; bolunen >= bolen; bolunen -= bolen) {
            bolum++;
            
        } 
        kalan = bolunen;  
        return bolum;
    }

int main() {
    

    

printf("%d\n", bol(456, 7));

    return 0;
}
