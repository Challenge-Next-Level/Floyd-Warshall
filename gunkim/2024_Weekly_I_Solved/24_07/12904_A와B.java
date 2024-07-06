// 문자열을 감미한 간단한 구현?
// StringBuilder를 통해 문자열 reverse하는 법을 알게 됨
import java.io.*;
import java.util.*;

public class Main {

    static private String S;
    static private String T;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        S = br.readLine();
        T = br.readLine();

        // T에서 S를 만들자 (문자를 제거하는 방향으로 진행하면 된다)
        while (T.length() > S.length()) {
            int tLen = T.length();
            if (T.charAt(tLen - 1) == 'A') {
                T = T.substring(0, tLen - 1);
            } else {
                T = T.substring(0, tLen - 1);
                StringBuilder sb = new StringBuilder(T);
                T = sb.reverse().toString();
            }
        }

        // 출력
        if (S.equals(T)) System.out.println(1);
        else System.out.println(0);

    }


}