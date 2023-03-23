int solution(int n) {
    int hrs = n / 60;
    int mins = n % 60;
    String clock_time = hrs + "" + mins;
    String[] chars = clock_time.split("");
    int total=0;
    for (String ch : chars){
        int num = Integer.parseInt(ch);
        total+=num;
    }
    return total;
}
