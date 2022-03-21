import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class DetailedCalculation extends CalculationTemplate
{
    private double sum;
    private double mean;
    private double median;
    private double std;
    private double mode;
    private double max;
    private double min;

    private double values[];

    DetailedCalculation(String filename)
    {
        values = new double[35];
        readInValues(filename);
    }

    private void readInValues(String filename)
    {
        try {
            File f = new File("src/main/resources/" + filename);

            Scanner s = new Scanner(f);

            int i = 0;
            while (s.hasNextDouble()) {
                values[i] = s.nextDouble();
                i++;
            }

            s.close();

        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    @Override
    public void calculate()
    {
        sum = sum();
        mean = mean();
        median = median();
        std = std();
        mode = mode();
        max = max();
        min = min();
    }

    @Override
    public void displayData()
    {
        System.out.println("Statistics");
        System.out.println("Sum: " + sum);
        System.out.println("Mean: " + mean);
        System.out.println("Median: " + median);
        System.out.println("Standard Deviation: " + std);
        System.out.println("Mode: " + mode);
        System.out.println("Max: " + max);
        System.out.println("Min: " + min);
    }

    private double sum()
    {
        double sum = 0.0;

        for (double d : values) {
            sum += d;
        }

        return sum;
    }

    private double mean()
    {
        return(Arrays.stream(values).average().orElse(Double.NaN));
    }

    private double median()
    {
        boolean isOdd = (values.length % 2 == 1);
        int length = values.length;

        if (isOdd) {
            return values[length / 2];
        } else {
            double sum = values[length / 2 - 1] + values[length / 2];
            double result = sum / 2.0;

            return result;
        }
    }

    private double std()
    {
        int length = values.length;
        double mean = mean();
        double std = 0.0;

        for (double d : values) {
            std += Math.pow(d - mean, 2);
        }

        return Math.sqrt(std / length);
    }

    private double mode()
    {
        double mode = values[0];
        int highestCount = 0;


        for (double d : values) {
            int count = 0;

            for (double d2 : values) {
                if (d == d2)
                    count++;
            }

            if (count > highestCount) {
                highestCount = count;
                mode = d;
            }
        }

        return mode;
    }

    private double max()
    {
        double max = values[0];

        for (double d : values) {
            if (d > max)
                max = d;
        }

        return max;
    }

    private double min()
    {
        double min = values[0];

        for (double d : values) {
            if (d < min)
                min = d;
        }

        return min;
    }

    public double[] test()
    {
        double[] testArray = new double[7];

        testArray[0] = sum;
        testArray[1] = mean;
        testArray[2] = median;
        testArray[3] = std;
        testArray[4] = mode;
        testArray[5] = max;
        testArray[6] = min;

        return testArray;
    }
}


