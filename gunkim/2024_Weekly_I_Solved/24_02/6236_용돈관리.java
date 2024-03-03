import java.util.*;
import java.io.*;

public class Main {


    private int[] money;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        money = new int[n];
        int maxMoney = 0;
        int totalMoney = 0;
        for (int i = 0; i < n; i++) {
            money[i] = Integer.parseInt(br.readLine());
            maxMoney = Math.max(maxMoney, money[i]);
            totalMoney += money[i];
        }

        // left는 무조건 maxMoney 보다는 커야한다. 그래야 인출했을 때 돈을 사용할 수 있음
        int left = maxMoney;
        int right = totalMoney;
        int answer = 0;
        while (left <= right) {
            // 인출 금액
            int mid = (left + right) / 2;

            // 인출 금액을 꺼내 쓸텐데 m번 안에 꺼내서 쓸 수 있는지 확인
            if (m >= isPossible(mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);

    }

    public int isPossible(int withdrawalAmount) { // withdrawalAmount : 인출 금액
        int count = 1;
        int used = withdrawalAmount;

        for (int m : money) {
            // 기본적으로 남은 금액이 있다면 해당 금액에서 사용을 한다
            used -= m;

            // 그런데 돈이 모자라면 남은 금액은 통장에 다시 넣어야 함
            // 돈을 다시 인출하여 해당 금액에서 사용한다
            if (used < 0) {
                count++;
                used = withdrawalAmount - m;
            }
        }
        // 돈을 몇 번 인출하는지 리턴
        return count;
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}