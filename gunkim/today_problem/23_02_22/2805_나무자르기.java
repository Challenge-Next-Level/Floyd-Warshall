// 처음에 틀렸습니다가 나온 이유: m의 최댓값이 2,000,000,000 이라 자료형을 long으로 선언해주었다.
import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        long m = Integer.parseInt(st.nextToken());

        int[] trees = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0, right = Arrays.stream(trees).max().getAsInt();
        int answer = 0;
        while (left <= right) {
            int mid = (left + right) / 2;
            long length = 0;
            for (int i = 0; i < n; i++) {
                length += Math.max((trees[i] - mid), 0);
            }
            if (length >= m) {
                left = mid + 1;
                answer = Math.max(answer, mid);
            } else right = mid - 1;
        }

        System.out.println(answer);
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}