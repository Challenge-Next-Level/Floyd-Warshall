//위상 정렬에 대해 알고 있으면 풀 수 있는 문제다.
import java.util.*;
import java.io.*;


public class Main {


    private int n;
    private int[] inDegree;
    private ArrayList<Integer>[] node;
    private ArrayList<Integer> answer;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        //pd의 출연순서 저장
        ArrayList<Integer>[] pd = new ArrayList[m];
        for (int i = 0; i < m; i++) {
            pd[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            for (int j = 0; j < num; j++) {
                pd[i].add(Integer.parseInt(st.nextToken()));
            }
        }
        //연결 정보 저장
        node = new ArrayList[n + 1];
        inDegree = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            node[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < pd[i].size() - 1; j++) {
                int start = pd[i].get(j);
                int end = pd[i].get(j + 1);
                node[start].add(end);
                inDegree[end]++;
            }
        }
        //위상 정렬
        answer = new ArrayList<>();
        bfs();
        int size = answer.size();
        if (size != n) System.out.println(0);
        else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < answer.size(); i++) {
                sb.append(answer.get(i) + "\n");
            }
            System.out.println(sb);
        }
    }

    public void bfs() {
        boolean[] visit = new boolean[n + 1];
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        for (int i = 1; i < n + 1; i++) {
            if (inDegree[i] == 0) {
                dq.add(i);
                visit[i] = true;
            }
        }


        while (!dq.isEmpty()) {
            int num = dq.pollFirst();
            answer.add(num);
            for (int i = 0; i < node[num].size(); i++) {
                int cur = node[num].get(i);
                if (!visit[cur]) {
                    inDegree[cur]--;
                    if (inDegree[cur] == 0) {
                        dq.add(cur);
                        visit[cur] = true;
                    }
                }
            }
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}