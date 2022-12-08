import java.io.*;
import java.util.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = "";
        StringBuilder sb = new StringBuilder();
        // EOF 처리
        // 백준에서는 파일 입력을 하기에 null 값이 들어가지만
        // intellij에서는 enter를 통한 입력이 들어가기에 isEmpty()를 통한 검사가 필요
        while ((input = br.readLine()) != null && !input.isEmpty()) {
            StringTokenizer st = new StringTokenizer(input);
            String s = new String(st.nextToken());
            String t = new String(st.nextToken());
            int sLen = s.length(), tLen = t.length();
            int sIdx = 0, tIdx = 0;
            while (tIdx < tLen) {
                if (sIdx >= sLen) break;
                if (s.charAt(sIdx) == t.charAt(tIdx)) sIdx += 1;
                tIdx += 1;
            }

            if (sIdx >= sLen) sb.append("Yes\n");
            else sb.append("No\n");
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}