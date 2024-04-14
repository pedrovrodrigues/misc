#include <stdio.h>
#include <math.h>

double EPSILON = 0.0000001;

double calc(double x, int p, int q, int r, int s, int t, int u){
    // p ∗ e−x + q ∗ sin(x) + r ∗ cos(x) + s ∗ tan(x) + t ∗ x2 + u = 0
    double res = 0;
    res += p * exp(-1*x);
    res += q * sin(x);
    res += r * cos(x);
    res += s * tan(x);
    res += t * x * x;
    res += u;
    return res;
}

double solve(double ini, double ini_val, double end, double end_val, int p, int q, int r, int s, int t, int u){
    double mid = (ini+end)/2;
    double mid_val = calc(mid, p,q,r,s,t,u);
    if(fabs(ini_val) < EPSILON)
        return ini;
    if(fabs(end_val) < EPSILON)
        return end;
    if(fabs(mid_val) < EPSILON)
        return mid;
    if(ini_val*mid_val <= 0)
        return solve(ini, ini_val, mid, mid_val, p,q,r,s,t,u);
    if(end_val*mid_val <= 0)
        return solve(mid, mid_val, end, end_val, p,q,r,s,t,u);
    return -1;
}

int main() {
    int n_cases;
    int p,q,r,s,t,u;
    double ini_val, end_val, root;

    scanf("%d", &n_cases);
    for(int i = 0; i < n_cases; i++){
        scanf("%d %d %d %d %d %d", &p, &q, &r, &s, &t, &u);
        ini_val = calc(0.0, p,q,r,s,t,u);
        end_val = calc(1.0, p,q,r,s,t,u);
        if(fabs(ini_val) < EPSILON)
            root = 0.0;
        else if(fabs(end_val) < EPSILON)
            root = 1.0;
        else        
            root = solve(0.0, ini_val, 1.0, end_val, p, q, r, s, t, u);
        if (root == -1) 
            printf("Sem solucao\n");
        else{
            // printf("%.9lf\n", root);
            // printf("%.8lf\n", root);
            // printf("%.7lf\n", root);
            // printf("%.6lf\n", root);
            // printf("%.5lf\n", root);
            printf("%.4lf\n", root);
            // printf("%.3lf\n", root);
        }
    }

    return 0;
}