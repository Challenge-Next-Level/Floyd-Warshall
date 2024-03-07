import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        int[] visitor = new int[n + 1];
        visitor[0] = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            visitor[i] = visitor[i - 1] + Integer.parseInt(st.nextToken());
        }

        int maxVisitor = 0;
        int count = 0;
        for (int i = 0; i <= n - x; i++) {
            int num = visitor[i + x] - visitor[i];
            if (num > maxVisitor) { // 최다 누적 방문자수 갱신
                maxVisitor = num;
                count = 1;
            } else if (num == maxVisitor) { // 같다면 갯수 증가
                count++;
            }
        }

        if (maxVisitor == 0) {
            System.out.println("SAD");
        } else {
            System.out.println(maxVisitor);
            System.out.println(count);
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}