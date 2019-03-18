import java.util.*;

/**
 * Created by Chris on 11/9/2018.
 */
public class PrintDuplicateString {
    public static void main(String[] args) {
        printdups("Hello");
        printdups("This is christopher");
        printdups("How are you doing today?");
    }
    private static void printdups(String s) {
        char[] chars = s.toCharArray();
        Map<Character, Integer> charMap = new HashMap<>();
        for (Character e : chars)
            if (charMap.containsKey(e))
                charMap.put(e, charMap.get(e) + 1);
            else
                charMap.put(e, 1);
        Set<Map.Entry<Character, Integer>> entrySet = charMap.entrySet();
        System.out.printf("List of duplicate characters in String '%s' %n", s);
        for (Map.Entry<Character, Integer> entry : entrySet) {
            if (entry.getValue() > 1) {
                System.out.printf("%s : %d %n", entry.getKey(), entry.getValue());
            }
        }
    }
}

/**
 Solution2
 Scanner scan = new Scanner(System.in);
 String s = scan.nextLine();
 String[] dups = new String[128];
 for(int i = 0; i < dups.length; i++)
 dups[i] = "";

 for(int i = 0; i < s.length(); i++)
 {
 dups[(int)(s.charAt(i))] += s.charAt(i);
 }
 for(int i = 0; i < 128; i++)
 if(dups[i]!="")
 if(dups[i].length()>1)
 System.out.println(dups[i]);
 */