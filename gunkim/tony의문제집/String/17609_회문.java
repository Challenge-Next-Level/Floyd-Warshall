import java.io.*;
import java.util.*;

public class Main {

    public Boolean check(int left, int right, String S) {
        while (left <= right) {
            if (S.charAt(left) != S.charAt(right)) return Boolean.FALSE;
            left += 1;
            right -= 1;
        }
        return Boolean.TRUE;
    }
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int test = Integer.parseInt(br.readLine());
        for (int i = 0; i < test; i++) {
            String word = new String(br.readLine());
            int size = word.length();
            int left = 0, right = size - 1, possible = 0; // possible에 회문(0),유사회문(1),일반회문(2) 를 저장
            while (left <= right) { // 양 끝 지점에 대해 탐색
                if (word.charAt(left) == word.charAt(right)) {
                    left += 1;
                    right -= 1;
                } else { // 최초로 다른 지점을 찾는다.
                    possible = 1; // 회문은 될 수 없음, 유사회문으로 설정
                    if (!check(left, right - 1, word) && !check(left + 1, right, word)) {
                        possible = 2;
                    }
                    break;
                }
            }
            sb.append(possible + "\n");
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}