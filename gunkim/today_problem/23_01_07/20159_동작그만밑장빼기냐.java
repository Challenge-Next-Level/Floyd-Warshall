import java.util.*;
import java.io.*;

public class Main {

    public int n;
    public int[] cards;
    public int answer = Integer.MIN_VALUE;

    //dp를 구하기 위해 점화식을 잘 세워야 하는 문제이다.
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        cards = new int[n + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) { //1~n 번 카드 초기화
            cards[i] = Integer.parseInt(st.nextToken());
        }

        int[][] sum = new int[2][n + 1]; //누적합을 저장. 0행: 짝수 번째, 1행: 홀수 번째 누적합
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                sum[0][i / 2] = sum[0][i / 2 - 1] + cards[i];
            }
            else{
                sum[1][i / 2 + 1] = sum[1][i / 2] + cards[i];
            }
        }

        for (int i = 1; i <= n; i++) { //i번째 카드를 밑장 빼기 할 때(해당 순서의 사람에게 밑장을 뺀 카드를 준다)
            int result;
            if (i % 2 == 0) result = sum[1][i / 2] + (sum[0][n / 2 - 1] - sum[0][i / 2 - 1]);
            else result = sum[1][i / 2] + cards[n] + (sum[0][n / 2 - 1] - sum[0][i / 2]);
            answer = Math.max(answer, result);
        }

        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}