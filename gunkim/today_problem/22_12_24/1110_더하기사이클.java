import java.util.*;
import java.io.*;

public class Main {

    public int makeSum(int num) {
        if (num < 10) {
            return num;
        } else {
            return (num / 10) + (num % 10);
        }
    }
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int num = n;
        int answer = 0;
        while (true) {
            int makeNum = makeSum(num);
            int newNum = (num % 10) * 10 + (makeNum % 10);
            answer++;
            if (newNum == n) {
                break;
            }
            num = newNum;
        }
        System.out.println(answer);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}