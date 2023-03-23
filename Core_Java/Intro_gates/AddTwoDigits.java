int solution(int n) {
    String st = Integer.toString(n);
    //System.out.println(st);
    int param1 = Integer.parseInt(st.substring(0,1));
    int param2 = Integer.parseInt(st.substring(1));
    //System.out.println("this is the first parameter" + param1);
    //System.out.println("this is the second parameter" + param2);
    return param1 + param2;
}
