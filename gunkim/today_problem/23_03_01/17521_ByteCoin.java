//수익을 최대로 얼만큼 벌 수 있는지 예측을 하지는 않았으나 꽤 커지는 것 같다
//int 자료형으로는 풀리지 않아 long으로 크기를 늘렸다.
import java.util.*;
import java.io.*;

public class Main {


    private int n;
    private long w;
    private int[] price;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());

        price = new int[n];
        for (int i = 0; i < n; i++) {
            price[i] = Integer.parseInt(br.readLine());
        }

        long coins = 0;
        int day = 0;
        while (day < n - 1) {
            if (price[day] < price[day + 1]) {
                long buy = w / price[day];
                coins += buy;
                w -= buy * price[day];
            } else if (price[day] > price[day + 1]) {
                if (coins != 0) {
                    w += price[day] * coins;
                    coins = 0;
                }
            }
            day++;
        }
        if (coins != 0) {
            w += price[day] * coins;
        }
        System.out.println(w);

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}