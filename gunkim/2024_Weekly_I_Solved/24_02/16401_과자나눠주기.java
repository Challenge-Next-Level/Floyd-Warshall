import java.util.*;
import java.io.*;

public class Main {


    private int[] cookie;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        cookie = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            cookie[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(cookie);


        int left = 1;
        int right = cookie[n - 1];
        int answer = 0;
        while (left <= right) {

            int mid = (left + right) / 2;

            int count = 0; // 몇 개의 과자를 나눠줄 수 있는가
            for (int i = 0; i < n; i++) {
                count += cookie[i] / mid;
            }

            if (count >= m) {
                answer = Math.max(answer, mid);
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(answer);

    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}