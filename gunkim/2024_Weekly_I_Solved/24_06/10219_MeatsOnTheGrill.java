// 해 구성하기 라는 알고리즘 분류
import java.util.*;
import java.io.*;

public class Main {


    private int h;
    private int w;
    private String[] board;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            h = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            board = new String[h];

            for (int j = 0; j < h; j++) {
                board[j] = br.readLine();
            }

            // board를 역순으로 출력하자(아래에서 위로)
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < h; j++) {
                sb.append(board[h - j - 1]).append('\n');
            }

            System.out.println(sb);
        }

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}