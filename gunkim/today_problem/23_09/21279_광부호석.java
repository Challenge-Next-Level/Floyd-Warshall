// 100_000 크기의 배열을 선언하여 모든 좌표에서의 가질 수있는 광물 갯수, 아름다움 정도를 저장하려 했음. 물론 c를 넘는 곳은 break
// for 문 2개를 사용했기에 너무 많은 메모리를 사용해 heap의 Out of Memory가 발생했음
// 모든 좌표를 하나씩 계산하는 방법 보단, x좌표 한 줄씩 탐색을 하며 최대 아름다움 값을 계산해 나가는 방법을 선택함
// PriorityQueue를 이용해 y좌표가 큰 값을 빼면서 c가 넘지 않게 직사각형을 유지해 나가면 된다
import java.util.*;
import java.io.*;

public class Main {


    public static final int MAX_SIZE = 100_001;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        ArrayList<Info>[] xIndex = new ArrayList[MAX_SIZE];
        for (int i = 0; i < MAX_SIZE; i++) {
            xIndex[i] = new ArrayList<>();
        }

        // x좌표를 기준으로 광물 정보를 저장한다
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            long v = Integer.parseInt(st.nextToken());
            xIndex[x].add(new Info(y, x, v));
        }

        long answer = 0;
        PriorityQueue<Info> q = new PriorityQueue<>();
        long currentV = 0L;
        for (int i = 0; i < MAX_SIZE; i++) {
            if (xIndex[i].isEmpty()) continue; // 존재하는 광물이 없다면
            for (int j = 0; j < xIndex[i].size(); j++) { // 같은 x선에 있는 좌표들을 모두 추가
                q.add(xIndex[i].get(j));
                currentV += xIndex[i].get(j).value;
            }

            int prevTop = -1;
            // 위에서 좌표들을 계속 추가하다 보면 c갯수를 넘을 수 있음
            while (q.size() > c) {
                prevTop = q.peek().y; // 가장 큰 y좌표를 무조건 빼야함
                currentV -= q.poll().value;
                // 이때 없앤 y좌표와 같은 선상에 광물들고 모두 빼야함
                while (!q.isEmpty() && q.peek().y == prevTop) {
                    currentV -= q.poll().value;
                }
            }

            // x좌표를 증가시킬 때 마다 정답 갱신 시도
            answer = Math.max(answer, currentV);
        }

        System.out.println(answer);

    }

    public class Info implements Comparable<Info> {
        private int y;
        private int x;
        private long value;

        public Info(int y, int x, long value) {
            this.y = y;
            this.x = x;
            this.value = value;
        }

        @Override
        public int compareTo(Info o) {
            return o.y - this.y;
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}