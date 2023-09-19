// 처음엔 '백 트래킹'만 이용해서 문제를 해결했음. 시간 초과 발생
// dp가 필요함을 느꼈고 해당 박스를 골랐을 때의 값으로 dp 갱신을 했음. 성공!
import java.util.*;
import java.io.*;

public class Main {


    private int n;
    private int[] boxes;
    private int[] dp;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        boxes = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            boxes[i] = Integer.parseInt(st.nextToken());
        }

        // dp 계산
        dp = new int[n];
        for (int i = 0; i < n; i++) {
            dfs(i, 1);
        }

        // 정답 도출
        int answer = 0;
        for (int i = 0; i < n; i++) {
            answer = Math.max(answer, dp[i]);
        }

        System.out.println(answer);
    }

    // 현재 사용한 박스 index, 선택된 박스 총 갯수
    public void dfs(int current, int count) {
        if (dp[current] >= count) return;
        dp[current] = count;

        for (int i = current + 1; i < n; i++) {
            if (boxes[i] <= boxes[current]) continue;
            dfs(i, count + 1);
        }

    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}