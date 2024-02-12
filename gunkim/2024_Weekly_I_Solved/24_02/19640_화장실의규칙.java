// 클래스를 불필요하게 2개 정의했음. Person에 그냥 lineIdx를 바로 넣어주는게 맞음
// 처음에 '시간 초과'를 받았음. 이유는 매번 PriorityQueue를 새로 만들었기 때문
// 선두주자를 한명 뺐을 때 바로 한 명을 PriorityQueue에 추가하면 되는 식으로 수정
import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Deque<Person>[] lines = new ArrayDeque[m + 1];
        for (int i = 1; i <= m; i++) {
            lines[i] = new ArrayDeque<>();
        }
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int days = Integer.parseInt(st.nextToken());
            int urgent = Integer.parseInt(st.nextToken());
            boolean isDeka = false;
            if (i == k + 1) isDeka = true;

            int idx = i % m;
            if (idx == 0) idx = m;
//            System.out.println(idx + " " + days + " " + urgent + " " + isDeka);
            lines[idx].add(new Person(days, urgent, isDeka));
        }

        PriorityQueue<Head> pq = new PriorityQueue<>();
        for (int j = 1; j <= m; j++) {
            if (!lines[j].isEmpty()) {
                Person person = lines[j].peekFirst();
                pq.add(new Head(j, person.days, person.urgent, person.isDeka));
            }
        }

        for (int i = 1; i <= n; i++) {
            Head head = pq.poll();
            lines[head.lineIdx].pollFirst();
            if (head.isDeka) {
                System.out.println(i - 1);
                break;
            }
            if (!lines[head.lineIdx].isEmpty()) {
                Person person = lines[head.lineIdx].peekFirst();
                pq.add(new Head(head.lineIdx, person.days, person.urgent, person.isDeka));
            }
        }

    }

    public class Person {
        private int days;
        private int urgent;
        private boolean isDeka;

        public Person(int days, int urgent, boolean isDeka) {
            this.days = days;
            this.urgent = urgent;
            this.isDeka = isDeka;
        }
    }

    public class Head implements Comparable<Head> {
        private int lineIdx;
        private int days;
        private int urgent;

        public Head(int lineIdx, int days, int urgent, boolean isDeka) {
            this.lineIdx = lineIdx;
            this.days = days;
            this.urgent = urgent;
            this.isDeka = isDeka;
        }

        @Override
        public int compareTo(Head o) {
            if (o.days != this.days) {
                return o.days - this.days;
            } else {
                if (o.urgent != this.urgent) {
                    return o.urgent - this.urgent;
                } else {
                    return this.lineIdx - o.lineIdx;
                }
            }
        }

        private boolean isDeka;
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}