// 풀이 과정은 완전 수학이다.
// 구간합은 sum[j] - sum[i]
// 구하려는 구간은 결국 (sum[j] - sum[i]) % M = 0 을 만족해야 함
// (중요) 모듈러 연산은 분배 가능함. sum[j]%M - sum[i]%M = 0
// sum[j]%M = sum[i]%M 을 구하면 된다.
// 이때, 나머지가 0인 경우(sum[i]%M = 0)는 j가 필요 없음. 카운트를 따로 더 한다.
import java.io.*;
import java.util.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int sum = 0;
        long[] remainder = new long[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            sum = (sum + Integer.parseInt(st.nextToken())) % m; // 부분합을 구한다. 모듈러 m을 적용하면서.
            remainder[sum] += 1; // 나머지가 0 ~ (m-1) 인 경우를 카운트
        }

        long answer = 0;
        answer += remainder[0]; // 부분합의 나머지가 0인 경우 추가
        for (int i = 0; i < m; i++) { // 부분합의 나머지가 같은 경우들에 대해 만들 수 있는 경우의 수 모두 추가
            answer += remainder[i] * (remainder[i] - 1) / 2;
        }
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}