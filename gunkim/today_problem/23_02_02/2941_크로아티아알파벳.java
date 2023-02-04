import java.util.*;
import java.io.*;

public class Main {

    private int index;
    private int result;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        index = 0;
        int length = str.length();
        result = 0;
        while (index < length) {
            char ch = str.charAt(index);
            if (ch >= 'a' && ch <= 'z') {
                if (ch == 'c' && index + 1 < length) {
                    if (str.charAt(index + 1) == '=' || str.charAt(index + 1) == '-') increaseValue(2);
                    else increaseValue(1);
                }
                else if (ch == 'd' && index + 2 < length) {
                    if (str.charAt(index + 1) == 'z' && str.charAt(index + 2) == '=') increaseValue(3);
                    else increaseValue(1);
                } else if (ch == 'l' && index + 1 < length && str.charAt(index + 1) == 'j') increaseValue(2);
                else if (ch == 'n' && index + 1 < length && str.charAt(index + 1) == 'j') increaseValue(2);
                else if (ch == 's' && index + 1 < length && str.charAt(index + 1) == '=') increaseValue(2);
                else if (ch == 'z' && index + 1 < length && str.charAt(index + 1) == '=') increaseValue(2);
                else increaseValue(1);
            } else index += 1;
        }
        System.out.println(result);
    }

    public void increaseValue(int idx) {
        index += idx;
        result += 1;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}