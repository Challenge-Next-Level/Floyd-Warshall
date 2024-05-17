// 자료형이 중요했던 문제
import java.util.*;
import java.io.*;

public class Main {

    private long x;
    private long y;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());

        int left = 0;
        int right = 1000000000;
        // 승률을 구하는 과정에서 값이 int 범위를 넘어가 long 형이 필요하다
        long z = (y * 100) / x;

        // 승률이 100%거나 99% 이상일 때는 더 이상 이겨도 변할 수 없음
        if (x == y || z >= 99) {
            System.out.println(-1);
            return;
        }

        int mid;
        int answer = Integer.MAX_VALUE;
        while (left <= right) {
            mid = (left + right) / 2;
            long newZ = ((y + mid) * 100) / (x + mid);
            if (z != newZ) {
                answer = Math.min(answer, mid);
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);

    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}