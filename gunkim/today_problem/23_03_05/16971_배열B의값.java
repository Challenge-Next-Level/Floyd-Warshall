import java.util.*;
import java.io.*;

public class Main {

    int[] rowSum, colSum;
    int[][] board, copyBoard;
    private int n;
    private int m;

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        for (int i = 0; i < n; i++) {// board 초기화
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        rowSum = new int[n];
        colSum = new int[m];
        for(int i = 0 ; i < n ; i++){//각 행, 열들의 합을 구한다
            for(int j = 0 ; j < m ; j++){
                rowSum[i] += board[i][j];
                colSum[j] += board[i][j];
            }
        }

        int rowMinValue = Integer.MAX_VALUE; //'가장 작은 row의 합'
        int minValueRow = -1; //'가장 작은 row의 합'을 가리키는 row
        int colMinValue = Integer.MAX_VALUE;
        int minValueCol  = -1;

        // 가장 합이 작은 row 탐색
        for(int r = 1 ; r < n - 1 ; r++){
            int val = rowSum[r];
            val *= 4;
            val -= 2 * (board[r][0] + board[r][m - 1]);

            if(rowMinValue > val){
                rowMinValue = val;
                minValueRow = r;
            }
        }

        // 가장 합이 작은 col 탐색
        for(int c =  1 ; c < m -1 ; c++){
            int val = colSum[c];
            val *= 4;
            val -= 2 * (board[0][c] + board[n - 1][c]);

            if(colMinValue > val){
                colMinValue = val;
                minValueCol = c;
            }
        }

        int answer = calculateB(board);

        if(minValueRow > 0) {// swap할 수 있는 row가 있다면
            setCopyBoard(true, 0, minValueRow); //0번 째 행과 swap
            answer = Math.max(answer, calculateB(copyBoard));

            setCopyBoard(true, n - 1, minValueRow); //(n-1)번 째 행과 swap
            answer = Math.max(answer, calculateB(copyBoard));
        }

        if(minValueCol > 0) {// swap할 수 있는 col가 있다면
            setCopyBoard(false, 0, minValueCol);//0번 째 열과 swap
            answer = Math.max(answer, calculateB(copyBoard));

            setCopyBoard(false, m - 1, minValueCol);//(n-1)번 째 열과 swap
            answer = Math.max(answer, calculateB(copyBoard));
        }

        System.out.println(answer);
    }

    public int calculateB(int[][] input) {
        int res = 0;

        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < m - 1; j++)
                res += input[i][j] + input[i + 1][j] + input[i + 1][j + 1] + input[i][j + 1];

        return res;
    }

    public void setCopyBoard(boolean isRow, int idx1, int idx2){
        copyBoard = new int[n][m];
        for(int i = 0 ; i < n ; ++i){//board deep copy
            for(int j = 0 ; j < m ; ++j){
                copyBoard[i][j] = board[i][j];
            }
        }
        if(isRow) {// row swap
            for(int c = 0 ; c < m ; ++c){
                copyBoard[idx1][c] = board[idx2][c];
                copyBoard[idx2][c] = board[idx1][c];
            }
        } else {//col swap
            for(int r = 0 ; r < n ; ++r){
                copyBoard[r][idx1] = board[r][idx2];
                copyBoard[r][idx2] = board[r][idx1];
            }
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}