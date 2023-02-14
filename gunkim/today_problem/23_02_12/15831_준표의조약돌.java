//dp문제일줄 알았는데 알고리즘 분류에 '투포인터'라는 문구를 보고 풀었다
import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        String bridge = br.readLine();

        int left = 0;
        int right = 0;
        int answer = 0;
        int black = 0;
        int white = 0;
        int route = 0;
        while (left <= right && right < n) {
            if (bridge.charAt(right) == 'B') black++;
            else white++;
            route++;

            while (black > b && left < right) {
                if (bridge.charAt(left) == 'B') black--;
                else white--;
                left++;
                route--;
            }
            if (black <= b && white >= w) {
                answer = Math.max(answer, route);
            }
            right++;
        }
        System.out.println(answer);
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}