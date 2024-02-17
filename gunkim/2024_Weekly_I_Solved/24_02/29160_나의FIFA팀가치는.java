// 자료 구조를 잘 활용하면 좋은 문제
import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // '선수 번호'별로 우선순위큐 배열 생성
        PriorityQueue<Player>[] players = new PriorityQueue[12];
        for (int i = 1; i <= 11; i++) {
            // 각 번호 별로 우선순위큐에 의해 정렬
            // 이때 '선수 가치'를 기준으로 maxHeap 만들기
            players[i] = new PriorityQueue<>(new Comparator<Player>() {
                @Override
                public int compare(Player o1, Player o2) {
                    return o2.worth - o1.worth;
                }
            });
        }

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            players[p].add(new Player(p, w));
        }

        // 매년 반복
        for (int i = 0; i < k; i++) {
            // 각 포지션 별로 최고 몸값의 선수를 1씩 감소
            for (int j = 1; j <= 11; j++) {
                if (!players[j].isEmpty()) {
                    Player player = players[j].poll();
                    // 주의 몸값이 0이 될 수는 없음
                    players[j].add(new Player(player.position, player.worth == 1 ? 1 : player.worth - 1));
                }
            }

            // 마지막 년도에 선수 가치 계산
            if (i == k - 1) {
                int answer = 0;
                for (int j = 1; j <= 11; j++) {
                    if (!players[j].isEmpty()) {
                        answer += players[j].peek().worth;
                    }
                }
                System.out.println(answer);
            }
        }

    }

    public class Player {
        private int position;
        private int worth;

        public Player(int position, int worth) {
            this.position = position;
            this.worth = worth;
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}