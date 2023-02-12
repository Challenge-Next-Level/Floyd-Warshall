import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test = Integer.parseInt(br.readLine());
        for (int i = 0; i < test; i++) {
            int n = Integer.parseInt(br.readLine());
            HashMap<String, Integer> hashMap = new HashMap<>();
            for (int j = 0; j < n; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String st1 = st.nextToken();
                String st2 = st.nextToken();
                if (!hashMap.containsKey(st2)) {//각 의상의 갯수를 저장
                    hashMap.put(st2, 1);
                } else hashMap.put(st2, hashMap.get(st2) + 1);
            }
            int result = 1;
            //nCr 계산에서 r=1 이면 nCr = n
            //각 의상의 수 만큼 곱하면 됨. 단, 입지 않는 경우도 포함하여 (n + 1) 값을 곱한다.
            for (int val : hashMap.values()) {
                result *= (val + 1);
            }
            //모두 입지 않는 경우(맨몸)는 제외하고 경우의 수 출력
            System.out.println(result - 1);
        }
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}