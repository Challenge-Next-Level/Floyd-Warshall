//하나의 Coordinate 클래스를 만들어 멤버 변수로 time, route를 넣어 관리하며 bfs를 진행했지만 그 연산들이 많은 시간을 잡는 것 같음, 시간초과 발생
//단순하게 time으로 해당 좌표에 시간을 기록하고, parent로 이전 node의 위치 정보를 저장하며 bfs를 진행하면 큰 연산 없이 진행할 수 있음
import java.util.*;
import java.io.*;

public class Main {

    private int end;
    private int[] parent = new int[100001];
    private int[] time = new int[100001];

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());

        bfs(start);

        Stack<Integer> stack = new Stack<>();
        stack.push(end);
        int index = end;

        while (index != start) {
            stack.push(parent[index]);
            index = parent[index];
        }

        // 최종 출력
        StringBuilder sb = new StringBuilder();
        sb.append(time[end] - 1 + "\n");
        while (!stack.isEmpty()) {
            sb.append(stack.pop() + " ");
        }

        System.out.println(sb.toString());
    }

    private void bfs(int node) {
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(node);
        time[node] = 1;

        while (!q.isEmpty()) {
            int now = q.poll();

            if (now == end) return;

            for (int i=0; i<3; i++) {
                int next;

                if (i == 0)         next = now + 1;
                else if (i == 1)    next = now - 1;
                else                next = now * 2;

                if (next < 0 || next > 100000) continue;

                if (time[next] == 0) {
                    q.add(next);
                    time[next] = time[now] + 1;
                    parent[next] = now;
                }
            }
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}