int solution(int[] a) {
    String biSt;
    String[] binariesStrings = new String[a.length];
    int j = 0;
    
    for(int i=0; i < a.length; i++){
        String something = "";
        biSt = String.format("%8s", Integer.toBinaryString(a[i])).replaceAll(" ", "0");
        binariesStrings[j] = biSt;
        ++j;
        //System.out.print(" " + biSt);
        if(i+1==a.length){
            for(String k : binariesStrings)
                something= k + something;
            System.out.println(something);
            return  Integer.parseInt(something, 2);
        }
    }
    
    return 0;
}
