// 문제 이해만 하면 쉽게 풀 수 있는 문제
import java.io.*;
import java.util.*;

public class Main {

    static private char[][] board;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        board = new char[n][n];
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < n; j++) {
                board[i][j] = input.charAt(j);
            }
        }

        // 가로 체크
        int row = 0;
        for (int i = 0; i < n; i++) {
            int j = 0;
            while (j < n - 1) {
                if (board[i][j] == '.' && board[i][j + 1] == '.') {
                    row++;
                    while (j < n) {
                        if (board[i][j] == 'X') break;
                        j++;
                    }
                }
                j++;
            }
        }
        // 세로 체크
        int col = 0;
        for (int i = 0; i < n; i++) {
            int j = 0;
            while (j < n - 1) {
                if (board[j][i] == '.' && board[j + 1][i] == '.') {
                    col++;
                    while (j < n) {
                        if (board[j][i] == 'X') break;
                        j++;
                    }
                }
                j++;
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(row).append(' ').append(col);
        System.out.println(sb);
    }


}