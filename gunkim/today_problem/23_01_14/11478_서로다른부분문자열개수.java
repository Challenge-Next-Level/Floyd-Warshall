import java.util.*;
import java.io.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String words = br.readLine();
        Set<String> set = new HashSet<>();
        int size = words.length();
        for (int i = 0; i < size; i++) {
            for (int j = i; j < size; j++) {
                set.add(words.substring(i, j + 1));
            }
        }
        System.out.println(set.size());

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}