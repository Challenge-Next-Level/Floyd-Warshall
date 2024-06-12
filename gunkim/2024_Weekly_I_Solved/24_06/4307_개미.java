// 애드 혹 문제
// 최대값을 알아내는데 어려운 문제
import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int length = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());

            int[] location = new int[n];
            for (int j = 0; j < n; j++) {
                location[j] = Integer.parseInt(br.readLine());
            }

            // 최소값 구하기
            int minResult = Integer.MIN_VALUE;
            for (int j = 0; j < n; j++) {
                int mindist = Math.min(location[j], length - location[j]);
                minResult = Math.max(mindist, minResult);
            }
            // 최대값 구하기
            int maxResult = 0;
            for (int j = 0; j < n; j++) {
                maxResult = Math.max(maxResult, Math.max(location[j], length - location[j]));
            }


            sb.append(minResult).append(" ").append(maxResult).append("\n");

        }

        System.out.println(sb);

    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}