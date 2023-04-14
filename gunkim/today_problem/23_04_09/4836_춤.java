//60% 대에서 실패한다. 보기에는 로직을 잘 짠 것 같은데 도저히 반례를 못 찾겠다.
//통과한 분들도 없어서 구글에 검색해도 java 정답은 없다.
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  public void solution() throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String input = "";
    while ((input = br.readLine()) != null && input.length() != 0) {
      String[] list = input.split(" ");
      int size = list.length;
      boolean[] answer = new boolean[6];
      if (size < 3) {
        answer[2] = true;
//        System.out.println("2222222222222222");
      } else if (!list[size - 3].equals("clap") || !list[size - 2].equals("stomp") || !list[size - 1].equals("clap")) {
        answer[2] = true;
//        System.out.println("2222222222222222");
      }
      if (size < 1 || list[0].equals("jiggle")){
        answer[4] = true;
//        System.out.println("44444444444444");
      }

      int countDip = 0;
      int countTwirl = 0;
      int countHop = 0;
      for (int i = 0; i < size; i++) {
        if (list[i].equals("twirl")) countTwirl++;
        if (list[i].equals("hop")) countHop++;
        if (list[i].equals("dip")) {
          countDip++;
          if (i - 1 >= 0 && list[i - 1].equals("jiggle")) continue;
          if (i - 2 >= 0 && list[i - 2].equals("jiggle")) continue;
          if (i + 1 < size && list[i + 1].equals("twirl")) continue;
          answer[1] = true;
          list[i] = "DIP";
//          System.out.println("1111111111111111");
        }
      }
      if (countDip == 0) {
        answer[5] = true;
//        System.out.println("55555555555");
      }
      if (countTwirl > 0 && countHop == 0) {
        answer[3] = true;
//        System.out.println("55555555555");
      }

      int errorCnt = 0;
      for (int i = 1; i <= 5; i++) {
        if (answer[i]) errorCnt++;
      }
      int[] K = new int[errorCnt];
      int kIdx = 0;
      for (int i = 1; i <= 5; i++) {
        if (answer[i]) K[kIdx++] = i;
      }
      StringBuilder sb = new StringBuilder();
      if (errorCnt == 0) {
        sb.append("form ok:");
      } else {
        if (errorCnt == 1) {
          sb.append("form error " + K[0] + ":");
        } else if (errorCnt == 2) {
          sb.append("form errors " + K[0] + " and " + K[1] + ":");
        } else {
          sb.append("form errors");
          for (int i = 0; i < errorCnt; i++) {
            if (i < errorCnt - 2) sb.append(" " + K[i]);
            else if (i != 0 && i + 1 == errorCnt) sb.append(" and " + K[i] + ":");
            else sb.append(", " + K[i]);
          }
        }
      }
      for (int i = 0; i < size; i++) {
        sb.append(" " + list[i]);
      }
//      sb.append("\n");
      System.out.println(sb);
    }

  }

  public static void main(String[] args) throws IOException {
    new Main().solution();
  }

}