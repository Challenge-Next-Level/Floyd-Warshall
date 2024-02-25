import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        if (N <= K) { // 물병 갯수가 k보다 작다면 0 출력
            System.out.println(0);
            return;
        }


        int buy = 0; // 사야하는 물병 수
        while (true) {
            int count = 0;
            int copyN = N; // 물병 갯수를 복사
            while (copyN != 0) {
                if (copyN % 2 == 1) { // 물병이 홀수개라면 남는 하나는 합치지 않는 물병으로 제외하기
                    count += 1;
                }
                copyN /= 2; // 물병 합치기
            }
            if (count <= K) // 제외된 물병이 k 이하라면 끝!
                break;
            // 그게 아니라면 물병갯수를 추가해 늘려가기
            N += 1;
            buy += 1;
        }
        System.out.println(buy);
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}