// 이분탐색 문제에서 가져왔지만 보자마자 '투 포인터'밖에 생각이 안났음
import java.io.*;
import java.util.*;

public class Main {

  private int n;


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    n = Integer.parseInt(br.readLine());
    int[] numbers = new int[n];
    StringTokenizer st = new StringTokenizer(br.readLine());
    for(int i = 0 ; i < n ; i++){
      numbers[i] = Integer.parseInt(st.nextToken());
    }

    Arrays.sort(numbers);

    int result = 0;
    for(int i = 0 ; i < n ; i++){ // i는 타겟이 되는 숫자가 됨
      int left = 0;
      int right = n-1;
      while(true){
        // 현재 타겟(i)의 위치에 있는 경우
        if(left == i) left++;
        else if(right == i) right--;

        // 결과를 찾을 수 없다.
        if(left >= right) break;

        // 합이 더 크다면 더 작은 수와 더해주어야 하니까 왼쪽으로 움직이는 right 값을 변경
        if(numbers[left] + numbers[right] > numbers[i]) right--;
        else if(numbers[left] + numbers[right] < numbers[i]) left++;
        else{
          result++;
          break;
        }
      }
    }
    System.out.println(result);

  }




  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}