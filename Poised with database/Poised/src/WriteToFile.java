import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class WriteToFile {
    public WriteToFile(int indexToCheck, int arrayIndex, int refNumber, String newData) {


        String toRewriteFile = "";
        boolean flag = true;

        try{
            Scanner sc = new Scanner(new File("Project_details.txt")).useDelimiter("\n");

            // Reads file line for line and splits it into an array to work with the data
            int toCheck;
            while (sc.hasNextLine()) {
                String readFile = sc.nextLine();
                String[] toArray = readFile.split(", ");
                toCheck = Integer.parseInt(toArray[indexToCheck]);

                // Compares the user input with the first index of the array to find the project
                if (toCheck == refNumber) {
                    toArray[arrayIndex] = newData;
                }

                // String building to ad everything together and remove the brackets
                toRewriteFile += Arrays.toString(toArray).replace("[", "")
                        .replace("]", "") + "\n";
            }
            sc.close();
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
            // Set flag to false so that if there is an error the file will not be written
            flag = false;
        }

        //toRewriteFile.replace("[", "").replace("]", "");
        if (flag){
            try{
                BufferedWriter out = new BufferedWriter(new FileWriter("Project_Details.txt", false));
                out.write(toRewriteFile);
                out.close();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
