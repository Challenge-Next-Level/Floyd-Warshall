// 정해진 해결 방법을 찾아나가는데 생각보다 어렵다
// 시간을 써야해서 그런걸까... 귀찮음도 큰 것 같다
import java.util.*;
import java.io.*;

public class Main {


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb;
        int n = Integer.parseInt(br.readLine());

        // 모든 쌍의 차가 최대 갯수일 때
        // 등비수열은 모든 쌍의 차가 다른 값을 갖는다
        System.out.println((n * (n - 1)) / 2);
        sb = new StringBuilder();
        int num = 1;
        for (int i = 0; i < n; i++) {
            sb.append(num).append(' ');
            num *= 2;
        }
        System.out.println(sb);

        // 모든 쌍의 차가 최소 갯수일 때
        // 등차수열은 최소 갯수를 갖는다
        System.out.println(n - 1);
        sb = new StringBuilder();
        num = 1;
        for (int i = 0; i < n; i++) {
            sb.append(num).append(' ');
            num += 1;
        }
        System.out.println(sb);
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}