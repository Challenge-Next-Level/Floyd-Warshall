//long 형이 2^64 범위라는 것을 알게되는 문제였다. 첨에는 황당하게 큰 범위를 준거라 생각했다
//제곱 계산을 Math.pow()를 사용해야 제대로 계산되는 것 같다. 일반적인 곱셈은 계산 정확도가 떨어지는 것 같다.
import java.util.*;
import java.io.*;


public class Main {


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine());

        long start = 0;
        long end = n;
        long answer = Long.MAX_VALUE;
        while (start <= end) {
            long mid = (start + end) / 2;
            long val = (long) Math.pow(mid, 2);
            if (val >= n) {
                answer = Math.min(answer, mid);
                end = mid - 1;
            } else start = mid + 1;

        }
        System.out.println(answer);


    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}