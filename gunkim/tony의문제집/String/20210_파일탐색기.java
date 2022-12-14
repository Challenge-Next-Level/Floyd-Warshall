import java.io.*;
import java.util.*;

public class Main {

    public boolean isNum(char c) {
        if ('0' <= c && c <= '9')
            return true;
        return false;
    }
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] str = new String[N];

        for (int i = 0; i < N; i++) {
            str[i] = br.readLine();
        }
        Arrays.sort(str, new Comparator<String>() {

            @Override
            public int compare(String s1, String s2) {
                int len1 = s1.length();
                int len2 = s2.length();
                int i = 0, j = 0;
                for (; i < len1 && j < len2; i++, j++) {
                    char c1 = s1.charAt(i);
                    char c2 = s2.charAt(j);
                    // 숫자인지 체크
                    boolean numeric1 = isNum(c1);
                    boolean numeric2 = isNum(c2);

                    // 1. 둘다 숫자
                    if (numeric1 && numeric2) {
                        // 숫자 앞 0 갯수 세기
                        int cnt1 = 0, cnt2 = 0;
                        while (i < len1 && '0' == s1.charAt(i)) {
                            cnt1++;
                            i++;
                        }
                        while (j < len2 && '0' == s2.charAt(j)) {
                            cnt2++;
                            j++;
                        }

                        // 0을 제외한 숫자
                        StringBuilder sb1 = new StringBuilder();
                        StringBuilder sb2 = new StringBuilder();
                        while (i < len1 && '0' <= s1.charAt(i) && s1.charAt(i) <= '9') {
                            if ('0' <= s1.charAt(i) && s1.charAt(i) <= '9') sb1.append(s1.charAt(i));
                            i++;
                        }
                        while (j < len2 && '0' <= s2.charAt(j) && s2.charAt(j) <= '9') {
                            if ('0' <= s2.charAt(j) && s2.charAt(j) <= '9') sb2.append(s2.charAt(j));
                            j++;
                        }
                        i--;
                        j--;

                        // 1-1. 길이가 긴 것이 더 큰 숫자
                        if (sb1.length() > sb2.length())
                            return 1;
                        else if (sb2.length() > sb1.length())
                            return -1;
                        else { // 길이가 같을 경우 한자리씩 비교하며 두 수 비교
                            int a = 0, b = 0;
                            for (; a < sb1.length() && b < sb2.length(); a++, b++) {
                                if (sb1.charAt(a) > sb2.charAt(b)) return 1;
                                else if (sb1.charAt(a) < sb2.charAt(b)) return -1;
                            }

                            // 1-2. 숫자까지 같다면 0의 갯수가 작은순
                            if(cnt1 != cnt2)
                                return cnt1 - cnt2;
                        }
                    }
                    // 2. 둘다 문자
                    if (!numeric1 && !numeric2) {
                        // 같은 캐릭터값이 경우 무시
                        c1 = s1.charAt(i);
                        c2 = s2.charAt(j);
                        if (c1 == c2)
                            continue;

                        boolean isUpper1 = c1 - 'a' < 0 ? true : false;
                        boolean isUpper2 = c2 - 'a' < 0 ? true : false;

                        // 대,소문자 알파벳에 대해 0~25로 생각하기 (a와A 모두 0으로 같음)
                        int n1 = c1 - 'a' >= 0 ? c1 - 'a' : c1 - 'A';
                        int n2 = c2 - 'a' >= 0 ? c2 - 'a' : c2 - 'A';

                        // 둘다 대문자 이거나 둘다 소문자
                        if ((isUpper1 && isUpper2) || (!isUpper1 && !isUpper2)) {
                            return n1 - n2;
                        }
                        // c1 소문자 && c2대문자
                        if (!isUpper1 && isUpper2) {
                            // c1,c2가 같은 문자일 경우
                            if (n1 == n2) return 1;
                            // 다른 문자일 경우
                            return n1 - n2;
                        }
                        // c1 대문자 && c2소문자
                        if (isUpper1 && !isUpper2) {
                            // c1,c2가 같은 문자일 경우
                            if (n1 == n2) return -1;
                            // 다른 문자일 경우
                            return n1 - n2;
                        }
                    }

                    // 3. c1 문자, c2 숫자
                    if (!numeric1 && numeric2) {
                        return 1;
                    }
                    // 4. c1 숫자, c2 문자
                    if (numeric1 && !numeric2) {
                        return -1;
                    }
                }

                // 5. 어떤 문자열이 짧아서 비교가 그대로 끝날 수 있음
                // 같은 문자인데 뒤에 다른 문자열이 붙는경우 더 깉 문자열이 뒤로
                return len1 - len2;
            }
        });

        Arrays.stream(str).forEach(System.out::println);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}