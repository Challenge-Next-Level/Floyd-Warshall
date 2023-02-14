import java.util.*;
import java.io.*;

public class Main {


    private String target;
    private int targetSize;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        target = br.readLine();
        targetSize = target.length();
        int answer = 0;

        String[] str = new String[n];
        for (int i = 0; i < n; i++) {
            str[i] = br.readLine();
        }

        for (int i = 0; i < n; i++) {
            String old = str[i];
            int size = str[i].length();
            answer += isPossible(old, size);//문자열, 문자열 길이
        }

        System.out.println(answer);
    }

    public int isPossible(String old, int size) {
        for (int startIdx = 0; startIdx < size; startIdx++) {//첫 번째 문자 위치 찾기
            if (old.charAt(startIdx) == target.charAt(0)) {
                for (int endIdx = size - 1; endIdx > startIdx; endIdx--) {//마지막 문자 위치 찾기
                    if (old.charAt(endIdx) == target.charAt(targetSize - 1)) {
                        int gap = (endIdx - startIdx) / (targetSize - 1);//문자들 사이의 gap을 알아낸다
                        int cnt = 1;
                        while (cnt < targetSize) {//gap 만큼 움직이며 문자 체크
                            if (old.charAt(startIdx + gap * cnt) == target.charAt(cnt)) {
                                cnt++;
                            } else break;
                        }
                        if (cnt >= targetSize) return 1;//가능하다면 1리턴, 중복 방지를 위해 리턴을 해야 함
                    }
                }
            }
        }
        return 0;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}