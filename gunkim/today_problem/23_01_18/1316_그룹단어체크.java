import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test = Integer.parseInt(br.readLine());
        int answer = 0;
        for (int i = 0; i < test; i++) {
            String word = br.readLine();
            int[] isConnect = new int[26];//소문자 알파벳을 0~25 숫자로 저장
            isConnect[word.charAt(0) - 'a'] = 1; //첫 번째 문자 체크
            if (checker(word, isConnect)) answer += 1; //그룹 체크
        }
        System.out.println(answer);
    }

    private boolean checker(String str, int[] check) {
        for (int i = 1; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == str.charAt(i - 1)) {//이전 문자와 같다면
                check[c - 'a'] += 1;
            } else {
                if (check[c - 'a'] == 0) check[c - 'a'] += 1;//처음 보는 문자라면
                else return false;//이전 문자와 같지도 않고, 이미 봤던 문자라면
            }
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}