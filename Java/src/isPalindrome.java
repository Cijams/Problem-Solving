public class isPalindrome {
    public static void main(String[] args) {

        String s = "racecar";
        String t = "pineapple";
        test(s);
        test(t);
    }
    static void test(String s)
    {
        boolean test = true;
        for(int i = 0, j = s.length()-1; i < s.length(); i++, j--)
            if(!(s.charAt(i)==s.charAt(j)))
                test = false;
        System.out.println(test);
    }
}
