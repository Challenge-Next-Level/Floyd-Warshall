import java.io.*;
import java.util.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int test = Integer.parseInt(br.readLine());
        for (int i = 0; i < test; i++) {
            String w = new String(br.readLine());
            int k = Integer.parseInt(br.readLine());

            // 예외 처리(k가 1인 경우 답은 "1 1"로 정해져 있음. 해당 처리를 하지 않으면 아래 로직으로는 해결할 수 없음.
            if (k == 1) {
                sb.append(1 + " " + 1 + "\n");
                continue;
            }
            // 알파벳 별로 갯수를 카운트하여 저장
            HashMap<Character, Integer> map = new HashMap<>();
            for (int j = 0; j < w.length(); j++) {
                map.put(w.charAt(j), map.getOrDefault(w.charAt(j), 0) + 1);
            }
            // 문자열 탐색
            int minVal = Integer.MAX_VALUE;
            int maxVal = -1;
            for (int left = 0; left < w.length(); left++) {
                if (map.get(w.charAt(left)) < k) continue; // k개 이상의 알파벳을 가진 경우만 탐색
                int count = 1;
                for (int right = left + 1; right < w.length(); right++) {
                    if (w.charAt(right) == w.charAt(left)) count++;
                    if (count == k) {
                        minVal = Math.min(minVal, right - left + 1);
                        maxVal = Math.max(maxVal, right - left + 1);
                        break;
                    }
                }
            }
            if (maxVal == -1) sb.append(-1 + "\n");
            else sb.append(minVal + " " + maxVal + "\n");
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}