import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        ArrayList<Cost> costs = new ArrayList<>();
        int left = Integer.MAX_VALUE, right = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            costs.add(new Cost(a, b));
            left = Math.min(left, a);
            right = Math.max(right, a);
        }
        int profit = 0, answer = 0;
        for (int i = left; i <= right; i++) {
            int total = 0;
            for (Cost c : costs) {
                if (c.price >= i) {
                    if (i - c.delivery > 0) total += i - c.delivery;
                }
            }
            if (total > profit) {
                profit = total;
                answer = i;
            }
        }
        System.out.println(answer);

    }

    public class Cost {
        private int price;
        private int delivery;

        public Cost(int price, int delivery) {
            this.price = price;
            this.delivery = delivery;
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}