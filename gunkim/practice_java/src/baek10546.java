import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class baek10546 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Map<String, Integer> dict = new HashMap<>(); // dictionary 자료형인 HashMap 이용
        for (int i = 0; i < n; i++) {
            String name = sc.next();
            if (dict.get(name) != null) { // 동명이인의 사람 입력시 value += 1
                dict.put(name, dict.get(name) + 1);
            } else { // 처음 입력하는 사람일 때 value = 1
                dict.put(name, 1);
            }
        }
        for (int i=0; i<n-1; i++) { // 완주자 입력은 value -= 1
            String name = sc.next();
            dict.put(name, dict.get(name) - 1);
        }
        for (String key : dict.keySet()) { // value = 0 이 아닌 사람은 완주를 못한 것
            if (dict.get(key) > 0) {
                System.out.println(key);
                break;
            }
        }
    }
}