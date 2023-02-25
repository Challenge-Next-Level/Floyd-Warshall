//dfs로 푸는 방법은 '시간초과'를 유발, 물론 풀이가 있을 수는 있음
//bfs로 푸는 방법이 시간을 줄이는 방법이라 생각, 대신 visit을 3차 배열로 생성
//visit에서 해당 좌표에서 벽을 몇 번 부쉈는지 까지 체크하여 '방문 여부'를 저장
import java.util.*;
import java.io.*;

public class Main {


    private int[][] arr;
    private boolean[][][] visit;
    private int n, m, k;
    private int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    private int answer;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        visit = new boolean[n][m][k + 1];
        answer = -1;

        for(int i = 0; i < n; i++) {
            String str = br.readLine();
            for(int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(String.valueOf(str.charAt(j)));
            }
        }

        bfs();

        System.out.println(answer);

    }

    public class Info {
        private int y, x, broken, depth;

        public Info(int y, int x, int broken, int depth) {
            this.y = y;
            this.x = x;
            this.broken = broken;
            this.depth = depth;
        }
    }

    public void bfs() {
        Queue<Info> q = new ArrayDeque<>();
        q.offer(new Info(0, 0, 0, 1));
        visit[0][0][0] = true;

        while (!q.isEmpty()) {
            Info info = q.poll();

            if (info.y == n - 1 && info.x == m - 1) {
                if (answer == -1) answer = info.depth;
                else answer = Math.min(answer, info.depth);
                return;
            }

            for(int i = 0; i < dir.length; i++) {
                int curRow = info.y + dir[i][0];
                int curCol = info.x + dir[i][1];

                if(curRow < 0 || curRow >= n || curCol < 0 || curCol >= m) {
                    continue;
                }

                if(!visit[curRow][curCol][info.broken]) {
                    if (arr[curRow][curCol] == 1 && info.broken < k) {
                        q.offer(new Info(curRow, curCol, info.broken + 1, info.depth + 1));
                        visit[curRow][curCol][info.broken + 1] = true;
                    } else if (arr[curRow][curCol] == 0) {
                        q.offer(new Info(curRow, curCol, info.broken, info.depth + 1));
                        visit[curRow][curCol][info.broken] = true;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}