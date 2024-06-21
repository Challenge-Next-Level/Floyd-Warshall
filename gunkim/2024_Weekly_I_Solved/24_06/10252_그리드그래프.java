// 문제를 이해하는데 오래 걸림
// 행의 갯수가 짝수, 홀수일 때 생각해서 노가다로 작업
import java.util.*;
import java.io.*;

public class Main {


    private int m;
    private int n;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken()); // 행
            n = Integer.parseInt(st.nextToken()); // 열


            sb.append("1\n");
            if (m % 2 == 0) {
                for (int j = 0; j < m; j++) {
                    for (int k = 0; k < n; k++) {
                        if (j % 2 == 0) {
                            sb.append('(').append(j).append(',').append(k).append(")\n");
                        } else {
                            sb.append('(').append(j).append(',').append(n - k - 1).append(")\n");
                        }
                    }
                }
            } else {
                for (int j = 0; j < m; j++) {
                    for (int k = 1; k < n; k++) {
                        if (j % 2 == 0) {
                            sb.append('(').append(j).append(',').append(k).append(")\n");
                        } else {
                            sb.append('(').append(j).append(',').append(n - k).append(")\n");
                        }
                    }
                }
                for (int j = m - 1; j >= 0; j--) {
                    sb.append('(').append(j).append(',').append('0').append(")\n");
                }
            }

        }

        System.out.println(sb);
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}