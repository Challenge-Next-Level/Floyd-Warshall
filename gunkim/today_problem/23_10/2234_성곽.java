// 왜 골드 3 밖에 안되는지 의아한 문제
// 인접한 다른 방을 어떻게 알아내야 하는지 + 비트 연산의 부족한 실력 때문에 다른 분의 풀이를 참고함
// 중요한 포인트 3가지가 있다고 생각
// 1. 비트 연산은 &연산자를 통해 1,2,4,8 과 같은 숫자를 통해 간단히 할 수 있음 ex) 11 & 8 = 1 은 남쪽에 벽이 있다는 의미
// 2. 각 방을 탐색할 때 단순히 visit으로 체크하는 것이 아닌 num을 통해 서로 다른 번호를 부여해두는 것
// 3. 하나의 방을 탐색하다 인접한 다른 방을 탐색했을 때 그 정보를 미리 저장해두는 것. 이를 바탕으로 인접한 방이 무엇이 있는 지 쉽게 가져올 수 있음
import java.util.*;
import java.io.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    // input
    static int N, M,room =0, maxNum = 0;
    static int[][] map, wall;
    // bfs
    static Deque<int[]> deque;
    static int[] dx = { -1, 0, 1, 0 };
    static int[] dy = { 0, -1, 0, 1 };
    static int[] dir = { 1, 2, 4, 8 };
    static ArrayList<Integer> space =  new ArrayList(); // 방의 넓이 담기
    static HashMap<Integer, Set<Integer>> side = new HashMap<>(); // 키: 방 넘버 , 값: 근접해 있는 방들의 넘버



    public void solution() throws Exception {
        st = new StringTokenizer(br.readLine());

        // 보통 N을 row의 수로 쓰기 때문에 일부로 순서를 바꿔 값을 받았음
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        wall = new int[N][M]; // 벽에 대한 정보 저장

        // *** 두 번째로 중요한 포인트: 각 방은 다른 번호로 저장하여 구분한다
        map = new int[N][M]; // 방의 번호를 저장할 것이다
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                wall[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 1
        int num = 1; // 1번 방부터
        deque = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0) { // 탐색하지 않은 방이라면
                    bfs(i, j, num++); // 방 탐색, num은 해당 방의 번호가 될 것
                    room++; // 방 개수 증가
                }
            }
        }

        System.out.println(room); // 방 개수
        System.out.println(maxNum); // bfs에서 계속 갱신시킨 가장 넓은 방의 넓이

        int sum = 0; // 벽 하나 허물고 합친 넓이
        for (int i = 1; i <= room; i++) { // 1번방부터 room(방의 개수)번 방까지 살펴보면서
            if (side.get(i) != null) { // 인접한 방이 있으면
                for (int nextRoomNum : side.get(i)) { // 방의 넘버를 하나씩 받아온다
                    // (i번 방 + 인접한 방) 값을 구해와 sum 갱신
                    // i번 방의 크기 값이 space에 (i - 1)번 째에 저장되어 있기 때문에 -1을 하는 것
                    sum = Math.max(space.get(i - 1) + space.get(nextRoomNum - 1), sum);
                }
            }
        }
        System.out.println(sum);
    }

    private static void bfs(int y, int x, int num) {
        int nx, ny, cnt =0;
//        int[] pos = new int[2]; // 좌표값을 담을 배열
        deque.add(new int[] { y, x }); // {y, x} 좌표로 시작
        map[y][x] = num;
        Set<Integer> set = new HashSet<>(); // 인접한 방의 번호를 담을 set(중복 방지)
        while (!deque.isEmpty()) {
            int[] pos = deque.poll();
            y = pos[0];
            x = pos[1];
            cnt++; // 새로운 블럭에 올때마다 방의 넓이 증가
            for (int i = 0; i < 4; i++) { // 서, 북, 동, 남 순서
                ny = y + dy[i];
                nx = x + dx[i];
                if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;


                // *** 세 번째로 중요한 포인트: 인접한 방의 번호를 저장해두는 것
                if (map[ny][nx] != 0 && map[ny][nx] != num) { // 이미 방문한 다른 방이라면
                    set.add(map[ny][nx]); // set에 추가
                    continue;
                }

                // dir = {1, 2, 4, 8}; 서, 북, 동, 남 순서
                // *** 가장 중요한 포인트: 탐색을 할 때 벽이 아닌 곳을 찾아야 했고 비트 연산으로 가볍게 조건 처리 했다
                if ((wall[y][x] & dir[i]) == 0 && map[ny][nx] == 0) { // 비트 연산 true(벽이 아닐 때) + 아직 방문 안했으면
                    deque.add(new int[] { ny, nx });
                    map[ny][nx] = num;
                }
            }
        }
        side.put(num, set); // 키: num, 값: 인접한 방 세트
        space.add(cnt); // 방 넓이 담기
        maxNum = Math.max(maxNum, cnt); // 가장 넓은 방 넓이 갱신
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}