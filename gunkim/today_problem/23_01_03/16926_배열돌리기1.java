import java.util.*;
import java.io.*;

public class Main {

    public void RotateArray(int sy, int sx, int dy, int dx) { //좌상좌표, 우하좌표
        int firstVal = arr[sy][sx];
        //윗줄이동
        for (int i = sx; i < dx; i++) {
            arr[sy][i] = arr[sy][i + 1];
        }
        //우측줄이동
        for (int i = sy; i < dy; i++) {
            arr[i][dx] = arr[i + 1][dx];
        }
        //아랫줄이동
        for (int i = dx; i > sx; i--) {
            arr[dy][i] = arr[dy][i - 1];
        }
        //좌측줄이동
        for (int i = dy; i > sy; i--) {
            arr[i][sx] = arr[i - 1][sx];
        }
        arr[sy + 1][sx] = firstVal;
    }
    int[][] arr;
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        arr = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        //구간을 지정하는 걸 제대로 안해줘서 틀렸었음.
        int count = Math.min(n, m) / 2;
        for (int i = 0; i < count; i++) {
            for (int j = 0; j < r; j++) {
                RotateArray(i, i, n - i - 1, m - i - 1);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (j == m - 1) sb.append(arr[i][j] + "\n");
                else sb.append(arr[i][j] + " ");
            }
        }
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}