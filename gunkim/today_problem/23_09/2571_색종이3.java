// 누적합 개념을 사용하는데 이걸 높이에 적용하는 접근을 떠올릴 수가 없었음
// 그리고 다양한 풀이가 있었는데 [이 분의 풀이](https://zoosso.tistory.com/155)가 O(n^3)으로 푸는 가장 명쾌한 풀이었음
// 좌표를 0 ~ 99의 값을 쓰는게 헷갈렸음
import java.util.*;
import java.io.*;

public class Main {


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;

        // int 초기값은 0으로 자동 설정된다
        // 그리고 0 ~ 99의 좌표를 사용한다
        int[][] board = new int[100][100];
        for (int i = 0; i < n; i++) { // 보드판에 색종이가 붙은 위치 표시
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            for (int j = r; j < r + 10; j++) {
                for (int k = c; k < c + 10; k++) {
                    board[j][k] = 1;
                }
            }
        }

        // 각 줄의 최대 높이 설정하기
        for (int i = 1; i < 100; i++) { // 첫 째 줄은 건너뛰어도 된다
            for (int j = 0; j < 100; j++) {
                if (board[i][j] == 0) continue; // 빈 공간인 경우 건너 뛰기
                board[i][j] = board[i - 1][j] + 1;
            }
        }

        int answer = 0;
        // 각 지점에서 만들 수 있는 직사각형 찾아 최댓값 갱신하기
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) { // i, j는 시작 좌표
                if (board[i][j] == 0) continue;
                int height = 100;
                for (int k = j; k < 100; k++) { // 넓이를 늘려가며 가장 낮은 높이 찾기
                    height = Math.min(height, board[i][k]);
                    if (height == 0) break; // 빈 공간을 만난 경우 break
                    answer = Math.max(answer, height * (k - j + 1)); // 최대 넓이 갱신 시도
                }
            }
        }

        System.out.println(answer);
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}