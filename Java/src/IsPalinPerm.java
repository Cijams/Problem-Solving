import java.util.HashMap;

public class IsPalinPerm {
    public static void main(String[] args) {
        String s1 = "rrccaae"; // True, racecar
        String s2 = "Tact Cao"; // True, Taco Cat
        String s3 = "Trundle the Troll"; // False, supposedly...

        System.out.println(test(s1));
        System.out.println(test(s2));
        System.out.println(test(s3));
    }
    private static boolean test(String s) {
        s = s.replaceAll("\\s","");
        s = s.toLowerCase();
        HashMap<Character, Integer> hm = new HashMap<>();
        for(Character c : s.toCharArray()) {
            if(hm.putIfAbsent(c, 1) != null)
                hm.put(c, hm.get(c)+1);
        }
        int oddCount = 0;
        for(int i : hm.values())
            if(i % 2 != 0)
                oddCount += 1;
        return !(oddCount > 1);
    }
}
