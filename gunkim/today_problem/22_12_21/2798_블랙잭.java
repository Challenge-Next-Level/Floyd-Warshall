import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Integer n = Integer.parseInt(st.nextToken());
        Integer m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        Integer[] cards = new Integer[n];
        for (int i = 0; i < n; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (cards[i] + cards[j] + cards[k] > m) continue;
                    answer = Math.max(answer, cards[i] + cards[j] + cards[k]);
                }
            }
        }
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}