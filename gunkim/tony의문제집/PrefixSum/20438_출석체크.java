import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {

    public void makeArray(int size, int[] arr, StringTokenizer stringTokenizer) {
        for (int i = 0; i < size; i++) {
            arr[i] = Integer.parseInt(stringTokenizer.nextToken());
        }
    }

    public void makeSet(int size, HashSet<Integer> set, StringTokenizer stringTokenizer) {
        for (int i = 0; i < size; i++) {
            set.add(Integer.parseInt(stringTokenizer.nextToken()));
        }
    }
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        boolean[] student = new boolean[n+3]; // 초기값 false
        HashSet<Integer> sleep = new HashSet<Integer>();
        makeSet(k, sleep, new StringTokenizer(br.readLine()));
        int[] check = new int[q];
        makeArray(q, check, new StringTokenizer(br.readLine()));

        // 출석체크 진행
        for (int i = 0; i < q; i++) { // 코드를 받은 학생들
            int num = check[i];
            int idx = 1;
            if (sleep.contains(num * idx)) continue; // 코드 받은 사람이 자고 있다면 모두 보내지 못함
            while (num * idx < n + 3) {
                if (!sleep.contains(num * idx)) student[num * idx] = true;
                idx += 1;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) { // 각 구간들에 대한 확인
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int answer = 0;
            for (int j = s; j <= e; j++) {
                if (!student[j]) answer +=1;
            }
            sb.append(answer).append("\n");
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}