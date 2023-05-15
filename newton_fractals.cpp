#include<cmath>
#include<iostream>
#include <fstream>
#include<vector>
#include "complex.h"
#include "polynomials.h"
using namespace std;


int main(){
vector<double> coeff = {-1.0, 0.0, 1.0, 0.0, 1.0};
polynomial p(coeff);
complex guess;
double r = -2.0;
double i = 2.0;
const int res = 2048;
double inc = 4.0/(res-1);


ofstream results("fractal.txt");
for (int k=0; k<res; k++){
    i-=inc;
    for (int j=0; j<res; j++){
        r+=inc;
        guess.i = i;
        guess.r = r;
        results<<p.counter_find_root(guess)<<',';
    };
    results<<endl;
    r = -2.0;
};

results.close();

}