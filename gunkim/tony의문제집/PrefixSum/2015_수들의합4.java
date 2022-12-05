import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] sumA = new int[n + 1];
        HashMap<Integer, Long> dict = new HashMap<>();

        // 정답이 될 수 있는 경우가 매우 많을 수 있음. 따라서 long형 선언. int형은 시간 초과가 발생.
        long answer = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            sumA[i] = sumA[i - 1] + Integer.parseInt(st.nextToken());

            // (지금까지 누적합) = k 인 경우
            if (sumA[i] == k) answer += 1;
            // (지금까지 누적합) - (이전 어느 구간까지 누적합) = k 인 경우
            if (dict.containsKey(sumA[i] - k)) {
                answer += dict.get(sumA[i] - k);
            }

            // map에 경우 추가
            dict.put(sumA[i], dict.getOrDefault(sumA[i], 0L) + 1);
        }

        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}