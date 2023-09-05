// 구현 문제의 느낌이 강했다. 오랜만에 1try 1sol 했다.
// bfs를 적절히 활용하는 것과 내가 둬야할 바둑돌의 위치도 미리 저장하는 것이 핵심이었던 것 같음
import java.util.*;
import java.io.*;

public class Main {


    private static int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    private boolean[][] visit;
    private int n;
    private int m;
    private int[][] board;
    private List<Group> aiGroup;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }


        // 2로 이루어진 그룹 저장하기
        aiGroup = new ArrayList<>();
        visit = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 2 && !visit[i][j]) {
                    aiGroup.add(new Group(new Coordinate(i, j), bfs(i, j)));
                }
            }
        }

//        System.out.println(aiGroup.size());

        // 2의 옆자리(좌표)를 저장하기
        List<Coordinate> nextToAi = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visit[i][j] = false;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] != 2) continue; // ai 돌 옆 빈자리를 탐색하자
                for (int k = 0; k < 4; k++) {
                    int ny = i + dir[k][0];
                    int nx = j + dir[k][1];
                    if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
                    if (board[ny][nx] == 0 && !visit[ny][nx]) {
                        visit[ny][nx] = true;
                        nextToAi.add(new Coordinate(ny, nx));
                    }
                }
            }
        }

//        System.out.println(nextToAi.size());

        int length = nextToAi.size();
        int answer = 0;
        // 미리 저장한 돌을 놓을 위치(nextToAi)에 2개의 돌을 놓는 경우에 죽는 그룹을 알아낸다
        for (int i = 0; i < length; i++) {
            Coordinate first = nextToAi.get(i);
            board[first.y][first.x] = 1;
            if (i == length - 1) {
                // ai돌 바로 옆에 둘 수 있는 공간이 하나 밖에 없거나 하나만 옆에두는 경우
                answer = Math.max(answer, findDead());
            } else {
                for (int j = i + 1; j < length; j++) {
                    // 2개의 돌 모두 ai돌 바로 옆에 두는 경우
                    Coordinate second = nextToAi.get(j);
                    board[second.y][second.x] = 1;
                    answer = Math.max(answer, findDead());
                    board[second.y][second.x] = 0;
                }
            }
            board[first.y][first.x] = 0;
        }

        System.out.println(answer);
    }

    public int findDead() {
        // 모든 ai 그룹에 대해 0을 만나는지 체크한다
        int result = 0;
        for (int i = 0; i < aiGroup.size(); i++) {
            if (bfsZero(aiGroup.get(i))) // 죽는 그룹은 갯수를 추가한다
                result += aiGroup.get(i).count;
        }
        return result;
    }

    public boolean bfsZero(Group group) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visit[i][j] = false;
            }
        }
        Deque<Coordinate> deque = new ArrayDeque<>();
        Coordinate coordinate = group.start;
        visit[coordinate.y][coordinate.x] = true;
        deque.add(new Coordinate(coordinate.y, coordinate.x));

        while (!deque.isEmpty()) {
            Coordinate current = deque.pollFirst();
            for (int i = 0; i < 4; i++) {
                int ny = current.y + dir[i][0];
                int nx = current.x + dir[i][1];
                if (ny < 0 || ny >= n || nx < 0 || nx >= m || visit[ny][nx]) continue;

                if (board[ny][nx] == 0) return false; // 0을 만난다면 죽지 않는 그룹임
                if (board[ny][nx] == 2) {
                    visit[ny][nx] = true;
                    deque.add(new Coordinate(ny, nx));
                }
            }
        }
        return true; // 그룹에 인접한 곳에 0이 없다면 죽는 그룹
    }

    public int bfs(int y, int x) {
        Deque<Coordinate> deque = new ArrayDeque<>();
        visit[y][x] = true;
        int count = 1;
        deque.add(new Coordinate(y, x));

        while (!deque.isEmpty()) {
            Coordinate current = deque.pollFirst();
            for (int i = 0; i < 4; i++) {
                int ny = current.y + dir[i][0];
                int nx = current.x + dir[i][1];
                if (ny < 0 || ny >= n || nx < 0 || nx >= m || visit[ny][nx]) continue;

                if (board[ny][nx] == 2) {
                    visit[ny][nx] = true;
                    count++;
                    deque.add(new Coordinate(ny, nx));
                }
            }
        }
        return count;
    }


    public class Group {
        private Coordinate start;
        private int count;

        public Group(Coordinate start, int count) {
            this.start = start;
            this.count = count;
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