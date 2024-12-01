import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

import static java.lang.Integer.parseInt;

public class Main {
    public static void main(String[] args) {
        String filePath = "../input.txt";
        List<Integer> leftSide = new ArrayList<>();
        List<Integer> rightSide = new ArrayList<>();
        Integer totalDifference = 0;
        Integer similarityScore = 0;
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                leftSide.add(parseInt(parts[0]));
                rightSide.add(parseInt(parts[1]));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        Collections.sort(leftSide);
        Collections.sort(rightSide);
        for (int i = 0; i < leftSide.size() ; i++) {
            Integer lsv = leftSide.get(i);
            Integer rsv = rightSide.get(i);
            Integer answer = Math.abs(lsv - rsv);
            totalDifference += answer;
            long count = rightSide.stream().filter(num -> lsv.equals(num)).count();
            similarityScore += parseInt(String.valueOf(count)) * lsv;
        }
      System.out.printf(String.valueOf(totalDifference));
        System.out.printf("\n");
        System.out.printf(String.valueOf(similarityScore));
    }
}