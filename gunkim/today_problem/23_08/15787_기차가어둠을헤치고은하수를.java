// 간단한 구현 문제 + 이진수를 생각하여 풀었음
import java.io.*;
import java.util.*;

public class Main {



    public void solution() throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        boolean[][] trains = new boolean[n + 1][21];
        for (int i = 0; i < m; i++) { // 명령에 따라 기차에 승객 상,하차
            st = new StringTokenizer(br.readLine());
            int cmd = Integer.parseInt(st.nextToken());
            int idx = Integer.parseInt(st.nextToken());
            if (cmd == 1) {
                int num = Integer.parseInt(st.nextToken());
                if (!trains[idx][num]) trains[idx][num] = true;
            } else if (cmd == 2) {
                int num = Integer.parseInt(st.nextToken());
                if (trains[idx][num]) trains[idx][num] = false;
            } else if (cmd == 3) {
                if (trains[idx][20]) trains[idx][20] = false;
                for (int j = 20; j >= 2; j--) {
                    trains[idx][j] = trains[idx][j - 1];
                }
                trains[idx][1] = false;
            } else if (cmd == 4) {
                if (trains[idx][1]) trains[idx][1] = false;
                for (int j = 1; j <= 19; j++) {
                    trains[idx][j] = trains[idx][j + 1];
                }
                trains[idx][20] = false;
            }
        }

        Set<Integer> binary = new HashSet<>();
        int answer = 0;
        for (int i = 1; i <= n; i++) { // 기차에 승객이 앉은 상태를 '이진수'로 기록한다 ex) 100100 라고 생각
            int trainToBinary = 0;
            int idx = 1; // 이진수의 첫 자리는 1로 시작
            for (int j = 1; j <= 20; j++) {
                if (trains[i][j]) {
                    trainToBinary += idx;
                }
                idx *= 2; // 2를 곱해 자릿수를 올린다
            }
            // 만든 이진수가 set에 있는지 확인
            if (!binary.contains(trainToBinary)) {
                answer++;
                binary.add(trainToBinary);
            }
        }

        System.out.println(answer);
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}