// 분할정복일 수 밖에 없는 문제이지만 규칙을 찾는 것이 너무 어려웠다.
// 특히 중앙 검정색 타일 색칠에 대한 규칙 찾기가 가장 애매했다.
// * 검정 타일 조건 *
// 1. 이전 시간에 의해 검정색으로 칠해져 있는가?
// 2. 현재 시간에서 중앙(K x K)의 타일에 위치해 있는가?
// 분할 정복을 할 때 (r1,c1) ~ (r2,c2) 범위만 찾으면 되는 백트래킹을 활용했어야 하고
// 찾는 범위가 최대 50 * 50이라 정답 배열도 작게 할당하여 채워주면 되었다.

import java.util.*;
import java.io.*;

public class Main {

    static int s, n, k, r1, r2, c1, c2;
    static char[][] arr = new char[51][51];


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        s = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        r1 = Integer.parseInt(st.nextToken());
        r2 = Integer.parseInt(st.nextToken());
        c1 = Integer.parseInt(st.nextToken());
        c2 = Integer.parseInt(st.nextToken());

        divideAndConquer(0,0, (int) Math.pow(n, s), false);

        StringBuilder sb = new StringBuilder();
        // arr 배열에 저장한 정답을 출력
        for (int i = 0; i <= r2 - r1; i++) {
            for (int j = 0; j <= c2 - c1; j++) {
                sb.append(arr[i][j]);
            }
            sb.append("\n");
        }
        System.out.println(sb);

    }

    static void divideAndConquer(int y, int x, int size, boolean isBlack) {
        // (r1,c1) ~ (r2,c2) 범위에 해당하는 타일만 출력하자 [백트래킹]
        if (y > r2 || y + size <= r1 || x > c2 || x + size <= c1) return;
        if (size == 1) { // 타일 색칠하기
            // (r1,c1) ~ (r2,c2) 범위에 해당하는 타일을 arr에 저장
            if (isBlack) {
                arr[y - r1][x - c1] = '1';
            } else arr[y - r1][x - c1] = '0';
            return;
        }

        // 분할정복을 하기 위한 n크기 나누기
        int nSize = size / n;
        // 중앙에 k * k 크기 만큼은 검은색 타일이다.
        int blackStart = (n - k) / 2;
        int blackEnd = n - blackStart;
        for (int i = 0; i < n; i++) { // 분할을 할 때 n*n만큼으로 분할하여 정복하는 것이다.
            int ny = y + nSize * i;
            for (int j = 0; j < n; j++) {
                int nx = x + nSize * j;
                // 검은 타일 정하기. 이전에 검은 타일로 정해져 있었거나 현재 중앙(k * k)에 위치해 있으면 검정 타일
                if (isBlack || (i >= blackStart && i < blackEnd) && (j >= blackStart && j < blackEnd)) {
                    divideAndConquer(ny, nx, nSize, true);
                } else { // 그게 아니라면 흰색 타일
                    divideAndConquer(ny, nx, nSize, false);
                }
            }
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}