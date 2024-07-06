// ascii code를 이용한 형변환 문제랄까..?
import java.io.*;
import java.util.*;

public class Main {

    static private String str;
    static private int[] count = new int[26];


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        str = br.readLine();

        // 각 알파벳의 갯수를 카운트
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch >= 'A' && ch <= 'Z') {
                count[ch - 'A']++;
            } else {
                count[ch - 'a']++;
            }
        }

        // 갯수의 최댓값을 찾는다 + 최댓값을 갖는 알파벳 저장
        int maxVal = 0;
        int idx = -1;
        for (int i = 0; i < 26; i++) {
            if (count[i] > maxVal){
                maxVal = count[i];
                idx = i;
            }
        }

        // 갯수의 최댓값이 여러개인지 확인
        int cnt = 0;
        for (int i = 0; i < 26; i++) {
            if (count[i] == maxVal) cnt++;
        }

        // 출력
        if (cnt > 1) {
            System.out.println('?');
        } else System.out.println((char) (idx + 65));
    }


}