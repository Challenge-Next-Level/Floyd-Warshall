
import java.util.*;
import java.io.*;

public class Main {


    private int n;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        if (n % 2 == 0) {
            System.out.println("CY");
        } else {
            System.out.println("SK");
        }

    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}