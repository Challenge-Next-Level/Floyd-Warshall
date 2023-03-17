//투 포인터라는 힌트를 봐도 쉽게 접근할 수 없었음
//count를 통해 start index의 위치를 조정하는 아이디어가 좋았던 것 같음
import java.io.*;


public class Main {

  public void solution() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine());
    String str = br.readLine();

    int count = 0; //사용된 알파벳 수
    int start = 0, end = 0; //두 개의 포인터
    int answer = 0; //가장 큰 연속된 길이 저장
    int length = str.length();
    int[] alpha = new int[26]; //각 알파벳이 사용된 수 저장
    while (end < length) {
      //이동한 곳에 있는 알파벳 수 +1
      if (alpha[str.charAt(end) - 'a']++ == 0) count++;
      //count가 n을 넘지 않을 때 까지 start 조정
      while (start <= end && count > n) {
        if (--alpha[str.charAt(start) - 'a'] == 0) count--;
        start++;
      }
      //답 갱신
      answer = Math.max(answer, end - start + 1);
      end++;
    }
    System.out.println(answer);
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}