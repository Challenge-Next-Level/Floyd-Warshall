// 보자마자 슬라이딩 윈도우 문제라 생각했다
import java.io.*;
import java.util.*;

public class Main {

    static private int s;
    static private int p;
    static private int a;
    static private int c;
    static private int g;
    static private int t;
    static private int aCnt = 0;
    static private int cCnt = 0;
    static private int gCnt = 0;
    static private int tCnt = 0;
    static private int answer = 0;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력값 받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        s = Integer.parseInt(st.nextToken());
        p = Integer.parseInt(st.nextToken());

        String str = br.readLine();
        st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        g = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());

        // 첫 부분 문자열은 직접 찾는다
        for (int i = 0; i < p; i++) {
            checkAlpha(str.charAt(i));
        }
        isPossible();

        // 다음 부분 문자열은 자동화해서 찾는다
        for (int i = p; i < s; i++) {
            deleteAlpha(str.charAt(i - p));
            checkAlpha(str.charAt(i));
            isPossible();
        }

        System.out.println(answer);
    }

    public static  void checkAlpha(char ch) {
        if (ch == 'A') aCnt++;
        else if (ch == 'C') cCnt++;
        else if (ch == 'G') gCnt++;
        else if (ch == 'T') tCnt++;
    }

    public static  void deleteAlpha(char ch) {
        if (ch == 'A') aCnt--;
        else if (ch == 'C') cCnt--;
        else if (ch == 'G') gCnt--;
        else if (ch == 'T') tCnt--;
    }

    public static void isPossible() {
        if (aCnt >= a && gCnt >= g && cCnt >= c && tCnt >= t) {
            answer++;
        }
    }
}