// 애드 혹(게임 이론) 문제로 정말 신선한 충격을 안겨준 문제이다.
// 1은 굉장한 특수성을 갖게 된다
// 선공으로 시작하는 A에게 1은 바로 지웠을 때 딱 한 개만 지울 수 있게 하는 특별한 경우
// 다른 수를 지우더라도 1은 지워지는 특별한 경우
// 이렇게 2가지로써 활용된다
// 결국 1을 제외시키고 2~n 이라는 숫자를 가지고 둘이 게임을 했을 때
// A가 이긴다면 이기는 게임이고
// B가 이긴다면 처음 A가 1을 지움으로써 이기는 게임이 된다
// 따라서 n = 1 인 상황에서만 A가 지고 나머지 상황에서는 모두 A가 이기게 된다
import java.util.*;
import java.io.*;

public class Main {



    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        if (n == 1) System.out.println("B");
        else System.out.println("A");


    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}