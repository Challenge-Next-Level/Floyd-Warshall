// 왜 실버1 밖에 안되는지 의아한 문제
// dfs 개념은 바로 떠올랐지만 '알파벳의 갯수'를 이용해 결국 풀어야 했음
// ASCII에 대한 개념을 통해 int, char 형 변환도 자유자제로 활용할줄 알아야 해서 어려웠던 문제
import java.util.*;
import java.io.*;

public class Main {


    private int len;
    private String input;
    private int answer;
    private char[] alphabets;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        input = br.readLine();
        len = input.length();

        answer = 0;
        alphabets = new char[26];
        for (int i = 0; i < len; i++) { // 알파벳의 갯수를 각각 저장한다
            int ascii = input.charAt(i);
            alphabets[ascii - 'a']++;
        }

        // 알파벳의 갯수를 이용해 dfs로 문자열을 만든다
        dfs(0, "");

        System.out.println(answer);
    }

    public void dfs(int idx, String temp) {
        if (idx == len) {
            answer++;
            return;
        }

        for (int i = 0; i < 26; i++) {
            if (alphabets[i] == 0) continue;
            if (!temp.equals("") && temp.charAt(idx - 1) == (char)('a' + i)) continue;

            alphabets[i]--;
            dfs(idx + 1, temp + (char)('a' + i));
            alphabets[i]++;
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}