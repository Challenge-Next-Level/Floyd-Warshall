
import java.io.*;
import java.util.*;

public class Main {


    private boolean[][] blue;
    private boolean[][] green;
    private int score;

    public void solution() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        blue = new boolean[4][6];
        green = new boolean[6][4];
        score = 0;

        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            // 블록을 놓고 초록, 파랑으로 이동시킨다.
            moveInGreen(t, x, y);
            moveInBlue(t, x, y);

            // 점수 획득 여부를 체크한다.
            scoreInGreen();
            scoreInBlue();

            // 초록, 파랑 구역의 0,1행/열 부분을 체크한다.
            blockInGreenBlur();
            blockInBlueBlur();

        }

        int blockInBoard = 0;
        for (int i = 2; i <= 5; i++) {
            for (int j = 0; j < 4; j++) {
                if (green[i][j]) {
                    blockInBoard++;
                }
                if (blue[j][i]) {
                    blockInBoard++;
                }
            }
        }

        System.out.println(score);
        System.out.println(blockInBoard);
    }

    public void blockInGreenBlur() {
        // 0, 1 행에 존재하는지 확인
        int size = 2;
        boolean check = false;
        for (int i = 0; i < 2; i++) {
            if (check) break;
            for (int j = 0; j < 4; j++) {
                if (green[i][j]) {
                    size -= i;
                    check = true;
                    break;
                }
            }
        }
        // 존재한다면 블록을 이동시킨다(윗 줄로 업데이트 하면 된다)
        if (check) {
            for (int i = 5; i >= 2; i--) {
                for (int j = 0; j < 4; j++) {
                    green[i][j] = green[i - size][j];
                }
            }
            // 0, 1 행은 공백으로 둔다
            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < 4; j++) {
                    green[i][j] = false;
                }
            }
        }
    }

    public void blockInBlueBlur() {
        // 0, 1 열에 존재하는지 확인
        int size = 2;
        boolean check = false;
        for (int i = 0; i < 2; i++) {
            if (check) break;
            for (int j = 0; j < 4; j++) {
                if (blue[j][i]) {
                    size -= i;
                    check = true;
                    break;
                }
            }
        }
        // 존재한다면 블록을 이동시킨다(왼쪽 줄로 업데이트 하면 된다)
        if (check) {
            for (int i = 5; i >= 2; i--) {
                for (int j = 0; j < 4; j++) {
                    blue[j][i] = blue[j][i - size];
                }
            }
            // 0, 1 열은 공백으로 둔다
            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < 4; j++) {
                    blue[j][i] = false;
                }
            }
        }
    }

    public void scoreInGreen() {
        // 완성된 행을 체크
        int idx = -1;
        boolean bingo;
        for (int i = 5; i >= 2; i--) {
            bingo = true;
            for (int j = 0; j < 4; j++) {
                if (!green[i][j]){
                    bingo = false;
                    break;
                }
            }
            if (!bingo) continue;

            score++;
            if (idx == -1) idx = i;
            for (int j = 0; j < 4; j++) {
                green[i][j] = false;
            }
        }

        // 획득한 점수가 있다면 블록 정렬하고 점수 체크 다시 하기
        if (idx != -1) {
            for (int i = idx - 1; i >= 0; i--) {
                for (int j = 0; j < 4; j++) {
                    if (green[i][j]) {
                        if (j <= 2 && green[i][j + 1]) {
                            moveTwoBlockDown
                        }
                        moveBlockDown(i, j);
                    }
                }
            }
            scoreInGreen();
        }
    }

    public void moveBlockDown(int y, int x) {
        int idx = 5;
        while (idx >= 1) {
            if (!green[idx][x]) {
                green[idx][x] = true;
                green[y][x] = false;
                break;
            }
            idx--;
        }
    }

    public void scoreInBlue() {
        // 완성된 열을 체크
        int idx = -1;
        boolean bingo;
        for (int i = 5; i >= 2; i--) {
            bingo = true;
            for (int j = 0; j < 4; j++) {
                if (!blue[j][i]){
                    bingo = false;
                    break;
                }
            }
            if (!bingo) continue;

            score++;
            if (idx == -1) idx = i;
            for (int j = 0; j < 4; j++) {
                blue[j][i] = false;
            }
        }

        // 획득한 점수가 있다면 블록 정렬하고 점수 체크 다시 하기
        if (idx != -1) {
            for (int i = idx - 1; i >= 0; i--) {
                for (int j = 0; j < 4; j++) {
                    if (blue[j][i]) moveBlockRight(j, i);
                }
            }
            scoreInBlue();
        }
    }

    public void moveBlockRight(int y, int x) {
        int idx = 5;
        while (idx >= 1) {
            if (!blue[y][idx]) {
                blue[y][idx] = true;
                blue[y][x] = false;
                break;
            }
            idx--;
        }
    }

    public void moveInGreen(int t, int x, int y) {
        if (t == 1) {
            int idx = 0;
            while (idx <= 5) {
                if (idx == 5 || green[idx + 1][x]) {
                    green[idx][x] = true;
                    break;
                }
                idx++;
            }
        } else if (t == 2) {
            int idx = 0;
            while (idx <= 5) {
                if (idx == 5 || green[idx + 1][x]) {
                    green[idx][x] = true;
                    green[idx - 1][x] = true;
                    break;
                }
                idx++;
            }
        } else {
            int idx = 0;
            while (idx <= 5) {
                if (idx == 5 || green[idx + 1][x] || green[idx + 1][x + 1]) {
                    green[idx][x] = true;
                    green[idx][x + 1] = true;
                    break;
                }
                idx++;
            }
        }
    }

    public void moveInBlue(int t, int x, int y) {
        if (t == 1) {
            int idx = 0;
            while (idx <= 5) {
                if (idx == 5 || blue[y][idx + 1]) {
                    blue[y][idx] = true;
                    break;
                }
                idx++;
            }
        } else if (t == 2) {
            int idx = 0;
            while (idx <= 5) {
                if (idx == 5 || blue[y][idx + 1] || blue[y + 1][idx + 1]) {
                    blue[y][idx] = true;
                    blue[y + 1][idx] = true;
                    break;
                }
                idx++;
            }
        } else {
            int idx = 0;
            while (idx <= 5) {
                if (idx == 5 || blue[y][idx + 1]) {
                    blue[y][idx] = true;
                    blue[y][idx - 1] = true;
                    break;
                }
                idx++;
            }
        }
    }


    public class Coordinate {
        private int y;
        private int x;

        public Coordinate(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}