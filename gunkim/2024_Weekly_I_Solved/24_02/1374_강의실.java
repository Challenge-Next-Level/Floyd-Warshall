// 쉬운 PriorityQueue 문제
// 각각의 PriorityQueue에 정렬 순서를 정의하는 방법을 외워둘 필요가 있어 보임
import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());

        // 강의는 '시작 시간'을 기준으로 minHeap 만들기
        PriorityQueue<Lecture> lectures = new PriorityQueue<>(new Comparator<Lecture>() {
            @Override
            public int compare(Lecture o1, Lecture o2) {
                return o1.start - o2.start;
            }
        });

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int idx = Integer.parseInt(st.nextToken());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            lectures.add(new Lecture(idx, start, end));
        }

        // 강의실은 '종료 시간'을 기준으로 minHeap 만들기
        PriorityQueue<Lecture> classRoom = new PriorityQueue<>(new Comparator<Lecture>() {
            @Override
            public int compare(Lecture o1, Lecture o2) {
                return o1.end - o2.end;
            }
        });


        int answer = 0;
        // 모든 강의를 진행시킬 때
        for (int i = 0; i < n; i++) {
            Lecture lecture = lectures.poll();
            // 시작하려는 강의보다 일찍 끝난 강의들 제거하기
            while (!classRoom.isEmpty() && classRoom.peek().end <= lecture.start) {
                classRoom.poll();
            }
            // 강의 진행
            classRoom.add(lecture);
            answer = Math.max(answer, classRoom.size());
        }


        System.out.println(answer);

    }

    public class Lecture {
        private int idx;
        private int start;
        private int end;

        public Lecture(int idx, int start, int end) {
            this.idx = idx;
            this.start = start;
            this.end = end;
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}