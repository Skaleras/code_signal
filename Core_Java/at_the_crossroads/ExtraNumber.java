int solution(int a, int b, int c) {
    if (a==c & c==a) return b;
    else if (b==a & a==b) return c;
    else return a;
}
