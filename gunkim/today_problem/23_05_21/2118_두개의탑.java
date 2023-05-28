// 문제를 읽으면서 이해가 가지 않았음...
// 최초 '시간 초과' 결과를 받았었는데 answer 계산을 바로 하지 않고 각 노드별로 최대값을 저장해두고
// 마지막에 for문 한 번을 통해 계산을 했는데 이게 시간 초과를 유발했다...;;
import java.util.*;
import java.io.*;


public class Main {


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];
        int length = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            length += arr[i];
        }

        int answer = 0;
        for (int i = 0; i < n; i++) {
            int left = 0;
            int right = length;
            for (int j = 0; j < n - 1; j++) {
                int idx = (i + j) % n;
                left += arr[idx];
                right -= arr[idx];
                answer = Math.max(answer, Math.min(left, right));
                if (left >= right) break;
            }
        }

        System.out.println(answer);
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}