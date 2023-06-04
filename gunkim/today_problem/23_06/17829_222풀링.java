import java.util.*;
import java.io.*;

public class Main {

    private int n;
    private int[][] board;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = divideAndConquer(n, 0, 0);
        System.out.println(answer);

    }

    public int divideAndConquer(int size, int y, int x) {
        if (size == 2) {
            return pooling(board[y][x], board[y + 1][x], board[y][x + 1], board[y + 1][x + 1]);
        }
        int length = size / 2;
        int a = divideAndConquer(length, y, x);
        int b = divideAndConquer(length, y + length, x);
        int c = divideAndConquer(length, y, x + length);
        int d = divideAndConquer(length, y + length, x + length);
        return pooling(a, b, c, d);
    }

    public int pooling(int a, int b, int c, int d) {
        int max1 = Math.max(a, b);
        int max2 = Math.max(c, d);
        if (max1 > max2) {
            return Math.max(max2, Math.min(a, b));
        } else if (max1 < max2) {
            return Math.max(max1, Math.min(c, d));
        }
        return max1;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}