//그리디 알고리즘이란 걸 봐도 해결책이 떠오르지 않음. 아이디어가 번뜩 떠올려야 되는 문제 같음. 특히 그리디는...
import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String balls = br.readLine();
        int redBall = 0;
        int blueBall = 0;
        for (int i = 0; i < n; i++) {
            if (balls.charAt(i) == 'R') redBall += 1;
            else blueBall += 1;
        }

        int answer = Integer.MAX_VALUE;
        //빨간 공 좌측에 몰기
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (balls.charAt(i) == 'B') break;
            count += 1;
        }
        answer = Math.min(answer, redBall - count);
        //빨간 공 우측에 몰기
        count = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (balls.charAt(i) == 'B') break;
            count += 1;
        }
        answer = Math.min(answer, redBall - count);
        //파란 공 좌측에 몰기
        count = 0;
        for (int i = 0; i < n; i++) {
            if (balls.charAt(i) == 'R') break;
            count += 1;
        }
        answer = Math.min(answer, blueBall - count);
        //파란 공 우측에 몰기
        count = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (balls.charAt(i) == 'R') break;
            count += 1;
        }
        answer = Math.min(answer, blueBall - count);

        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}