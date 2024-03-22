// messi(N) = messi(N-1) + 1 + messi(N-2)
// 찾고 싶은 순번 m
// 1. m <= messi(N-1)
// 2. m == messi(N-1) + 1
// 3. m > messi(N-1) + 1
import java.io.*;
import java.util.*;

public class Main {

  public static long[] messi = new long[1000];
  public static int flag = 0;

  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    long M = Long.parseLong(br.readLine());

    // 글자 수 저장
    messi[1] = 5;
    messi[2] = 13;

    int index = 3;
    // 현재 주어진 M이 해당하는 messi의 index값(N값) 찾기
    while(true){
      messi[index] = messi[index - 1] + 1 + messi[index - 2];

      // 글자수가 m 을 넘으면 break
      if (messi[index] > M) {
        break;
      }

      index++;
    }

    find(index, M);
  }

  public static void find(int index, long n){
    if(flag==1){
      System.out.println("Messi Messi Gimossi");
      return;
    }
    if(index==1){
      System.out.println("Messi".charAt((int)n-1));
      return;
    }
    else if(index==2){
      // Messi Gimossi에서 공백을 만났을 경우
      if(n==6){
        System.out.println("Messi Messi Gimossi");
      }
      else
        System.out.println("Messi Gimossi".charAt((int)n-1));
      return;
    }

    // 앞 쪽에 해당하는 경우
    if(messi[index-1]>=n){
      find(index-1, n);
    }
    // 중간의 공백에 해당하는 경우
    else if(messi[index-1]+1==n){
      flag=1;
      find(index-1, n);
    }
    // 뒤 쪽에 해당하는 경우
    else{
      // 앞의 messi(n-1)과 공백의 크기를 전체 길이에서 빼주어야 한다.
      find(index-2, n-messi[index-1]-1);
    }

  }

  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}