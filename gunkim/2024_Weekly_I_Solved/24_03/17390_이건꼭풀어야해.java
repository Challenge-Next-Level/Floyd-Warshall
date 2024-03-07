import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[] arr = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i + 1] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        int[] cumulativeSum = new int[n + 1];
        cumulativeSum[0] = 0;
        for (int i = 1; i <= n; i++) {
            cumulativeSum[i] = cumulativeSum[i - 1] + arr[i];
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= q; i++) {
            st = new StringTokenizer(br.readLine());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());
            sb.append(cumulativeSum[right] - cumulativeSum[left - 1]).append("\n");
        }

        System.out.println(sb);
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}