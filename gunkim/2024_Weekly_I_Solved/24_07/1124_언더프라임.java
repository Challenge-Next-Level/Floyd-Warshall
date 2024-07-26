// 수학은 차갑다...
import java.io.*;
import java.util.*;

public class Main {

    static boolean[] prime = new boolean[100001];
    static int[] count = new int[100001];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        // 소수가 아닌 값은 true
        prime[0] = prime[1] = true;

        // 모든 구간의 수에 대해 소수 판별
        for (int i = 2; i < 100001; i++) {
            // 이미 탐색한 숫자이기에 continue
            if (prime[i]) continue;

            // 탐색한 숫자의 배수는 소수가 아니게 됨
            for (int j = i * 2; j < 100001; j += i) {
                prime[j] = true;

                // 숫자들에 대해 소인수분해를 하는 격
                // ex) 9 = 3 * 3 이므로 2개란 값을 count에 저장
                int tmp = j;
                while (tmp % i == 0) {
                    tmp /= i;
                    count[j]++;
                }
            }
        }

        int result = 0;
        for (int i = A; i <= B; i++) {
            // 1. 탐색 숫자가 몇 개로 소인수분해 되는가? count로 먼저 알아내기
            // 2. 그 갯수가 소수 값인가? prime으로 알아내기
            if (!prime[count[i]]) result++;
        }

        System.out.println(result);
    }

}