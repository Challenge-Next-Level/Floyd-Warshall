// 문제 설명이 다소 부족하다고 생각
// 한 칸씩 밖에 못가는 건지 제한없이 이동이 가능한지 애매해다
// 제한 없이 이동가능했고 각 지점마다 갈 수 있는지 dp로 저장하면 된다
import java.util.*;
import java.io.*;

public class Main {


    public void solution() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] A = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        boolean[] dp = new boolean[n + 1];
        dp[1] = true; // 시작 지점은 이동 가능한 곳
        for (int i = 1; i <= n - 1; i++) {
            if (!dp[i]) continue; // 올 수 없는 곳이라면
            for (int j = i + 1; j <= n; j++) {
                if (dp[j]) continue; // 올 수 있는 곳이라면, 굳이 계산하지 않음
                int cost = (j - i) * (1 + Math.abs(A[i] - A[j]));
                if (cost > k) continue; // 최대 비용을 넘는 cost가 필요하면
                dp[j] = true;
            }
        }

        if (dp[n]) System.out.println("YES");
        else System.out.println("NO");
    }





    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}