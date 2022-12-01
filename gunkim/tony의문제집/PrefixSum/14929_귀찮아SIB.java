import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        int[] num = new int[n + 1];
        int[] sum = new int[n + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            num[i] = Integer.parseInt(st.nextToken());
            sum[i] = sum[i-1] + num[i];
        }
        // int 크기로는 한계가 있다, '틀렸습니다'라는 결과가 나온다.
        long answer = 0;
        for (int i = 1; i < n; i++) {
            answer += num[i] * (sum[n] - sum[i]);
        }
        sb.append(answer);
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}