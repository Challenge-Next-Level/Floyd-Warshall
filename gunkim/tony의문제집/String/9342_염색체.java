import java.io.*;
import java.util.*;

public class Main {

    // 타겟 문자가 나온다면 인덱스 증가 시키기
    public Integer findWord(int size, int index, String word, Character gene) {
        while (index < size) {
            if (word.charAt(index) == gene) {
                index++;
            } else break;
        }
        return index;
    }

    // 타겟 문자를 찾았는지 인덱스의 변화로 확인
    public Boolean isFind(int beforeIdx, int afterIdx) {
        if (beforeIdx == afterIdx) return Boolean.FALSE;
        return Boolean.TRUE;
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        String word;
        for (int i = 0; i < t; i++) {
            word = new String(br.readLine());
            int idx = 0, size = word.length();
            // 첫 번째 문자 체크
            if (word.charAt(idx) != 'A') {
                Character ch = word.charAt(idx);
                if (ch == 'A' || ch == 'B' || ch == 'C' || ch == 'D' || ch == 'E' || ch == 'F') idx++;
                else {
                    sb.append("Good\n");
                    continue;
                }
            }
            // A 체크
            int movedIdx = findWord(size, idx, word, 'A');
            if (!isFind(idx, movedIdx)) {
                sb.append("Good\n");
                continue;
            }
            // F 체크
            idx = movedIdx;
            movedIdx = findWord(size, idx, word, 'F');
            if (!isFind(idx, movedIdx)) {
                sb.append("Good\n");
                continue;
            }
            // C 체크
            idx = movedIdx;
            movedIdx = findWord(size, idx, word, 'C');
            if (!isFind(idx, movedIdx)) {
                sb.append("Good\n");
                continue;
            }
            // 마지막 문자 체크
            if (movedIdx == size) sb.append("Infected!\n");
            else if (movedIdx == size - 1) {
                Character ch = word.charAt(movedIdx);
                if (ch == 'A' || ch == 'B' || ch == 'C' || ch == 'D' || ch == 'E' || ch == 'F') sb.append("Infected!\n");
                else sb.append("Good\n");
            } else sb.append("Good\n");
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}