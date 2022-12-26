import java.util.*;
import java.io.*;

public class Main {

    public class Lecture implements Comparable<Lecture> {
        private int start;
        private int end;

        public Lecture(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Lecture o) {
            return this.start - o.start;
        }
    }
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;

        List<Lecture> lectures = new ArrayList<>(); //lecture를 담는 리스트 초기화
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            lectures.add(new Lecture(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()))); //lecture추가
        }
        //강의 시작 순서로 정렬
        lectures.sort(Lecture::compareTo); //(s1,s2) -> s1.compareTo(s2)

        PriorityQueue<Integer> pq = new PriorityQueue<>(); //minHeap 사용
        pq.offer(lectures.get(0).end); //첫 강의실 미리 설정
        int answer = 1; //강의실의 갯수를 의미

        for (int i = 1; i < n; i++) {
            int nextStart = lectures.get(i).start; //다음 강의 시작 시간
            if (nextStart >= pq.peek()) { //pq.peek()이 nullPointException을 발생시킬 수 있지만 문제에선 그런 케이스를 제공x
                pq.poll();
            } else {
                answer++;
            }
            pq.offer(lectures.get(i).end);
        }
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}