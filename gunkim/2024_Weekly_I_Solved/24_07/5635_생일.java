// java 클래스의 Comparable를 통한 sort
import java.io.*;
import java.util.*;

public class Main {

    static private class Person implements Comparable<Person> {
        private String name;
        private int day;
        private int month;
        private int year;

        public Person(String name, int day, int month, int year) {
            this.name = name;
            this.day = day;
            this.month = month;
            this.year = year;
        }

        public int compareTo(Person o) {
            if (this.year != o.year) {
                return o.year - this.year;
            } else if (this.month != o.month) {
                return o.month - this.month;
            } else {
                return o.day - this.day;
            }
        }
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        Person[] people = new Person[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            people[i] = new Person(st.nextToken(),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()));
        }

        Arrays.sort(people);
        System.out.println(people[0].name);
        System.out.println(people[n - 1].name);
    }


}