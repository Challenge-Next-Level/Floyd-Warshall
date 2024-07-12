// 조금 귀찮았던 문제. 조건을 신경써서 답을 만들어야 한다
import java.io.*;
import java.util.*;

public class Main {

    static int N;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        String word = br.readLine(); // 첫 번째 단어
        int answer = 0;
        for (int i = 0; i < N - 1; i++) {
            String sWord = br.readLine(); // 비교 대상 단어

            // 길이가 2이상 차이나면 비슷한 단어 조차 될 수 없다
            if (Math.abs(word.length() - sWord.length()) >= 2) continue;

            boolean[] visit = new boolean[sWord.length()];
            int cnt = 0;
            for (int j = 0; j < word.length(); j++) { // 기준 단어의 알파벳이
                char ch = word.charAt(j);
                for (int k = 0; k < sWord.length(); k++) { // 비교 대상 단어에 포함되었는지 확인
                    if (visit[k]) continue;
                    if (ch == sWord.charAt(k)) {
                        visit[k] = true;
                        cnt++;
                        break;
                    }
                }
            }

            // 기존 단어와 비교 단어의 길이 비교에 따라 비슷한 단어가 되기 위한 cnt 조건이 달라짐
            if (word.length() == sWord.length()) {
                if (cnt == word.length() - 1 || cnt == word.length()) answer++;
            }
            else if (word.length() < sWord.length()) {
                if (cnt == word.length()) answer++;
            }
            else {
                if (cnt == word.length() - 1) answer++;
            }
        }

        System.out.println(answer);
    }



}