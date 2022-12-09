import java.io.*;
import java.util.*;

public class Main {

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String file = new String(br.readLine());
            String[] name = file.split("\\.");
            map.put(name[1], map.getOrDefault(name[1], 0) + 1);
        }
        map.keySet().stream().sorted().forEach(name -> System.out.println(name + " " + map.get(name)));
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}