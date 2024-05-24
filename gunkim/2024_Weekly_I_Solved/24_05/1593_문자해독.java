// 슬라이딩 윈도우 문제
import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int wLen = Integer.parseInt(st.nextToken());
    int sLen = Integer.parseInt(st.nextToken());

    String w = br.readLine();
    String s = br.readLine();

    int[] wArr = new int[52];
    int[] sArr = new int[52];

    // wArr에 w가 갖고 있는 문자를 카운트해서 넣어준다
    for (int i = 0; i < wLen; i++) {
      putWord(w.charAt(i), wArr, 1);
    }

    int answer = 0;
    // sArr에 s가 갖고 있는 문자를 카운트해서 넣어준다
    for (int i = 0; i < sLen; i++) {
      putWord(s.charAt(i), sArr, 1);

      // wLen 만큼 카운트해서 넣었다면 sArr와 wArr가 같은지 체크
      if (i >= wLen - 1) {
        if (Arrays.equals(wArr, sArr)) {
          answer++;
        }
        putWord(s.charAt(i - wLen + 1), sArr, -1);
      }
    }

    System.out.println(answer);

  }

  // 배열이 52크기
  // 0 ~ 25 까지는 소문자(a-z)
  // 26 ~ 51 까지는 대문자(A-Z)
  private void putWord(char word, int[] arr, int num) {
    if('a' <= word && word <= 'z') { // 소문자일 때
      arr[word - 'a'] += num;
    }else { // 대문자일 때
      arr[word - 'A' + 26] += num;
    }
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}