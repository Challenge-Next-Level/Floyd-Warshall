// 우선 다양한 풀이가 있는 문제 같음. 문제 자체는 쉬운데 머리가 돌아가지 않는 상태라 잘 해결하지 못함
// 몇 번 째 부터 출력할 수 없는 수인지 알아내야 함
// 만들 수 있는 숫자들을 모두 만든 뒤 찾아내도 되는 문제. 아래는 DFS로 가능한 수를 모두 만들었음
import java.io.*;
import java.util.*;
public class Main {

  private List<Long> list = new ArrayList<>();


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());

    if(n <= 10) {
      System.out.print(n);
      return;
    } else if (n >= 1023) {
      System.out.print(-1);
      return;
    }

    // 만들 수 있는 경우의 수를 모두 탐색하여 만든다
    for(int i = 0; i < 10; i++) {
      DFS(i);
    }
    // 모든 수를 저장한 리스트를 순서를 위해 정렬
    Collections.sort(list);
    // 출력
    System.out.print(list.get(n));

  }

  private void DFS(long num) {
    list.add(num);
    long modValue = num % 10; // 10으로 나눈 나머지 값
    if(modValue == 0) {
      return;
    }

    // 앞 번 째 숫자보다 작아야 하니까 -1 하고 시작
    for(long i = modValue - 1; i >= 0; i--) {
      long newValue = num * 10 + i;
      DFS(newValue);
    }
  }


  public static void main(String[] args) throws Exception {

    new Main().solution();
  }

}