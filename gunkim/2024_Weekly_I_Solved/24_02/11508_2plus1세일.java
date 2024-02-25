import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < n; i++) {
            pq.add(Integer.parseInt(br.readLine()));
        }

        int answer = 0;
        while (pq.size() >= 3) {
            answer += pq.poll();
            answer += pq.poll();
            pq.poll();
        }
        while (!pq.isEmpty()) {
            answer += pq.poll();
        }

        System.out.println(answer);

    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}