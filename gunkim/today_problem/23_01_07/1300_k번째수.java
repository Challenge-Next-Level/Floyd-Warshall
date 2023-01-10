import java.util.*;
import java.io.*;

public class Main {

    //문제의 답을 x라고 한다면, x 보다 작은 숫자가 k개 있다는 의미이다.
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        //찾고자 하는 수는 k보다 작을 수 밖에 없다.
        int low = 1;
        int high = k;
        while (low < high) {
            int mid = (low + high) / 2;
            int count = 0;

            for (int i = 1; i <= n; i++) {
                count += Math.min(mid / i, n);
            }

            if (count >= k) {//조건을 만족해도 최소값의 수를 찾는다
                high = mid;
            } else {//숫자를 키워가면서 수를 찾는다.
                low = mid + 1;
            }
        }
        System.out.println(low);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}