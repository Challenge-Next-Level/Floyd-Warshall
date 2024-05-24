// 제곱 결과를 long 형으로 바꾸면 틀렸던 문제
import java.io.*;
import java.util.*;

public class Main {


  public void solution() throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    long n = Long.parseLong(br.readLine());

    long start = 0;
    long end = n;
    long result=0;

    while(start<=end) {
      long mid = (start + end) / 2;
      if(n <= Math.pow(mid, 2)){
        result=mid;
        end=mid-1;
      }else{
        start=mid+1;
      }
    }

    System.out.println(result);

  }




  public static void main(String[] args) throws Exception {
    new Main().solution();
  }

}