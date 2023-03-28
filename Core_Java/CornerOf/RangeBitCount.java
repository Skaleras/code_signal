int solution(int a, int b) {
    int size = b - a + 1;
    String[] nums = new String[size];
    for(int i = 0; a <= b; i++){
        nums[i] = Integer.toBinaryString(a);
        a++;
    }
    /*System.out.println(nums); Ain't gonna work
    because in order to print an array in java,
    you have to loop over each element of the
    array to show it just like below*/
    int counter = 0;
    for(String num: nums)
        for(char ch : num.toCharArray())
            if(Character.getNumericValue(ch)==1)
                counter++;
    return counter;
    
    /*Option2 slightly more efficient
    for(String num : nums)
        counter+= num.length() - num.replaceAll("1", "").length();
    return counter;*/
}
