import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        // 큰 액수부터 사용하기 위해 maxHeap 만들기
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < n; i++) {
            pq.add(Integer.parseInt(br.readLine()));
        }

        int result = 0;
        int count = 0;
        // 목표 금액에 도달할 때 까지
        while (result != k) {
            int required = k - result; // 채우기 위해 필요한 돈
            int money = pq.poll(); // 사용하게 될 동전
            if (money > required) continue;
            int added = required / money;
            result += money * added;
            count += added;
        }

        System.out.println(count);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}