//날짜별로 팀을 만들어야 한다는 생각에 접근조차 못함
//팀을 반씩 나눠가며 서로 다른 팀을 만들면(분할정복을 이렇게 하면) 쉽게 만들 수 있었음
import java.io.*;


public class Main {

  private char[][] monkeys;

  public void solution() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(br.readLine());
    monkeys = new char[7][n];

    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < n; i++) {
      sb.append('A');
    }

    divideAndConquer(0, n - 1, 0);

    for (int i = 0; i < 7; i++) {
      String team = new String(monkeys[i]);
      //A로만 배정된 팀 배치를 바꿔주기 위함
      if(team.equals(sb.toString())){
        team = team.substring(1);
        team += "B";
      }
      System.out.println(team);
    }
  }

  //팀을 반 씩 쪼개면서 서로 다른 팀을 만들면 됨
  //7일이 되기도 전에 분할정복이 다 되면 A라는 팀만 모두 배정이 될거임
  public void divideAndConquer(int startIdx, int endIdx, int day) {
    if (day == 7) return;
    int mid = (startIdx + endIdx) / 2;
    for (int i = startIdx; i <= mid; i++) {
      monkeys[day][i] = 'A';
    }
    for (int i = mid + 1; i <= endIdx; i++) {
      monkeys[day][i] = 'B';
    }
    divideAndConquer(startIdx, mid, day + 1);
    divideAndConquer(mid + 1, endIdx, day + 1);
  }


  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}