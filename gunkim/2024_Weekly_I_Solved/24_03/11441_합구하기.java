import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] cumulativeSum = new int[n + 1]; // 누적합 저장 배열
        cumulativeSum[0] = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            cumulativeSum[i] = cumulativeSum[i - 1] + Integer.parseInt(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());
            // 구간 유의해서 누적합 출력하기
            System.out.println(cumulativeSum[right] - cumulativeSum[left - 1]);
        }


    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}