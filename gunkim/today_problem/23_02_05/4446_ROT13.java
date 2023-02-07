//EOF 에 대한 처리는 했지만, 정답까지 도달 할 수 없었음
//도대체 어떤 부분에서 반례가 있는지 모르겠음
import java.util.*;
import java.io.*;

public class Main {

    private final char[] vowel = {'a', 'i', 'y', 'e', 'o', 'u'};
    private final char[] consonant = {'b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f'};
    private StringBuilder sb;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = "";
        sb = new StringBuilder();
        while ((str = br.readLine()) != null && !str.isEmpty()) {
            if (sb.length() != 0) sb.append("\n");
            int size = str.length();
            int idx = 0;
            while (idx < size) {
                char ch = str.charAt(idx);
                if (ch >= 'a' && ch <= 'z') {
                    if (ch == 'a' || ch == 'i' || ch == 'e' || ch == 'o' || ch == 'u' || ch == 'y') {
                        findVowel(ch, true);
                    } else findConsonant(ch, true);
                } else if (ch >= 'A' && ch <= 'Z') {
                    if (ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U' || ch == 'Y') {
                        findVowel(ch, false);
                    } else findConsonant(ch, false);
                } else {
                    sb.append(ch);
                }
                idx++;
            }
        }
        System.out.println(sb);
    }

    private void findConsonant(char ch, boolean isLowerCase) {
        int index = 0;
        char lowerCaseCh = Character.toLowerCase(ch);
        while (index < consonant.length) {
            if (consonant[index] == lowerCaseCh) break;
            index++;
        }
        int findIdx = (index + 10) % consonant.length;
        if (isLowerCase) sb.append(consonant[findIdx]);
        else sb.append(Character.toUpperCase(consonant[findIdx]));
        return;
    }

    private void findVowel(char ch, boolean isLowerCase) {
        int index = 0;
        char lowerCaseCh = Character.toLowerCase(ch);
        while (index < vowel.length) {
            if (vowel[index] == lowerCaseCh) break;
            index++;
        }
        int findIdx = (index + 3) % vowel.length;
        if (isLowerCase) sb.append(vowel[findIdx]);
        else sb.append(Character.toUpperCase(vowel[findIdx]));
        return;
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}