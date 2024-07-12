// 복잡한 생각은 접고 contains를 이용해 탐색하면 되는 문제...
import java.io.*;
import java.util.*;

public class Main {


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        String p = br.readLine();

        int idx = 0;
        int cnt = 0;
        for (int i = 0; i < p.length(); i++) {
            // 탐색하는 구간의 문자열이 s에 있는지 확인
            // 있다면 continue를 통해 구간을 늘려간다
            if (s.contains(p.substring(idx, i + 1))) continue;

            // 없다면 copy 단계를 진행했다고 생각
            cnt++;
            idx = i;
        }
        System.out.println(cnt + 1);
    }


}