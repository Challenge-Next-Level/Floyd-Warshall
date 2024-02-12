// 쉬운 우선순위큐 문제
import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());

        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < n; i++) {
            int height = Integer.parseInt(br.readLine());
            pq.add(height);
        }

        int used = 0;
        while (t > 0 && pq.peek() >= h && pq.peek() != 1) {
            int top = pq.poll() / 2;
            pq.add(top);
            t--;
            used++;
        }

        if (pq.peek() < h) {
            System.out.println("YES");
            System.out.println(used);
        } else {
            System.out.println("NO");
            System.out.println(pq.peek());
        }

    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}