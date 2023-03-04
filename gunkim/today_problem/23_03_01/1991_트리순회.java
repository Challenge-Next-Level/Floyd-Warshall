import java.util.*;
import java.io.*;

public class Main {


    private HashMap<String, Node> map;
    private StringBuilder preorderSb;
    private StringBuilder inorderSb;
    private StringBuilder postorderSb;


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        map = new HashMap<>();
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            map.put(st.nextToken(), new Node(st.nextToken(), st.nextToken()));
        }

        preorderSb = new StringBuilder();
        preorder("A");
        inorderSb = new StringBuilder();
        inorder("A");
        postorderSb = new StringBuilder();
        postorder("A");
        System.out.println(preorderSb);
        System.out.println(inorderSb);
        System.out.println(postorderSb);

    }

    private void preorder(String node) {
        preorderSb.append(node);
        if (!map.get(node).left.equals(".")) {
            preorder(map.get(node).left);
        }
        if (!map.get(node).right.equals(".")) {
            preorder(map.get(node).right);
        }
    }

    private void inorder(String node) {
        if (!map.get(node).left.equals(".")) {
            inorder(map.get(node).left);
        }
        inorderSb.append(node);
        if (!map.get(node).right.equals(".")) {
            inorder(map.get(node).right);
        }
    }

    private void postorder(String node) {
        if (!map.get(node).left.equals(".")) {
            postorder(map.get(node).left);
        }
        if (!map.get(node).right.equals(".")) {
            postorder(map.get(node).right);
        }
        postorderSb.append(node);
    }
    public class Node {
        private String left;
        private String right;

        public Node(String left, String right) {
            this.left = left;
            this.right = right;
        }
    }



    public static void main(String[] args) throws Exception {
        new Main().solution();
    }

}