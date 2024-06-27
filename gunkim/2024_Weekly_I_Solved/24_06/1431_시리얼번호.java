// 돌고돌아 결국 클래스를 만들어 편리하게 정렬했음
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<SerialNumber> serialNumbers = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            int result = 0;
            for (char c : input.toCharArray()) {
                if (c >= '0' && c <= '9') {
                    result += c - '0';
                }
            }
            serialNumbers.add(new SerialNumber(input, input.length(), result));
        }

        Collections.sort(serialNumbers);
        for (int i = 0; i < n; i++) {
            System.out.println(serialNumbers.get(i).str);
        }
    }

    static class SerialNumber implements Comparable<SerialNumber> {
        private String str;
        private int length;
        private int sum;
        public SerialNumber(String str, int length, int sum) {
            this.str = str;
            this.length = length;
            this.sum = sum;
        }

        @Override
        public int compareTo(SerialNumber o) {
            if (this.length != o.length) {
                return this.length - o.length;
            }
            if (this.sum != o.sum) {
                return this.sum - o.sum;
            }
            return this.str.compareTo(o.str);
        }
    }
}