// '애드 혹'이란 카테고리로 분류된 알고리즘
// 구현 문제랑 비슷한 느낌 같다
import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        if (m + n - 1 > k) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
            StringBuilder sb = new StringBuilder();
            for (int i = 1; i <= n; i++) {
                for (int j = 0; j <= m - 1; j++) {
                    sb.append(i + j).append(" ");
                }
                sb.append("\n");
            }
            System.out.println(sb);
        }

    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}