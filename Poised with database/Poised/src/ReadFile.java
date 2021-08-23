import javax.swing.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class ReadFile {

    // Created a toString method to display the information for the user
    public String toString(String projectNumber, String projectName, String buildingType, String buildingAddress,
                           String erfNumber, String totalProjectCost, String totalPaidToDate, String deadline,
                           String projectCompleted, String customerName, String customerNumber,String customerEmail,
                           String customerAddress, String contractorName, String contractorNumber,
                           String contractorEmail, String contractorAddress, String architectName, String architectNumber,
                           String architectEmail, String architectAddress) {

        return JOptionPane.showInputDialog("Project details:\nThe project number is: " +projectNumber+
                "\nThe project name is: " +projectName+
                "\nThe type of building is: " +buildingType+
                "\nThe address of the building is: " +buildingAddress+
                "\nThe ERF number is: " +erfNumber+
                "\nThe total cost of the project is: R"+totalProjectCost+
                "\nWhat has being payed so far is: " +totalPaidToDate+
                "\nThe deadline of the project is: " +deadline+
                "\nHas the project being completed?: " +projectCompleted+
                "\n\nCustomer:\nThe name of the customer is: " +customerName+
                "\nThe number of the customer is: " +customerNumber+
                "\nThe e-mail of the customer is: " +customerEmail+
                "\nThe address of the customer is: " +customerAddress+
                "\n\nContractor:\nThe name of the contractor is: " +contractorName+
                "\nThe number of the contractor is: " +contractorNumber+
                "\nThe e-mail of the contractor is: " +contractorEmail+
                "\nThe address of the contractor is: " +contractorAddress+
                "\n\nArchitect:\nThe name of the architect is: " +architectName+
                "\nThe number of the architect is: " +architectNumber+
                "\nThe e-mail of the architect is: " +architectEmail+
                "\nThe address of the architect is: " +architectAddress);
    }

    /*
     Reads the file then splits it into an array
     Then slices the information into new variables to use the data as needed
     */
    public String readFile(int whatToView) {
        String output = "";
        String projectNumber;
        String projectName ;
        String buildingType ;
        String buildingAddress;
        String erfNumber;
        String totalProjectCost;
        String totalPaidToDate;
        String deadline;
        String projectCompleted;
        String customerName;
        String customerNumber;
        String customerEmail;
        String customerAddress;
        String contractorName;
        String contractorNumber;
        String contractorEmail;
        String contractorAddress;
        String architectName;
        String architectNumber;
        String architectEmail;
        String architectAddress;


        try{
            Scanner sc = new Scanner(new File("Project_Details.txt")).useDelimiter("\n");

            while (sc.hasNextLine()) {
                String read = sc.nextLine();
                String[] toArray = read.split(", ");
                projectNumber = toArray[0];
                projectName = toArray[1];
                buildingType = toArray[2];
                buildingAddress = toArray[3];
                erfNumber = toArray[4];
                totalProjectCost = toArray[5];
                totalPaidToDate = toArray[6];
                deadline = toArray[7];
                projectCompleted = toArray[8];
                customerName = toArray[9];
                customerNumber = toArray[10];
                customerEmail = toArray[11];
                customerAddress = toArray[12];
                contractorName = toArray[13];
                contractorNumber = toArray[14];
                contractorEmail = toArray[15];
                contractorAddress = toArray[16];
                architectName = toArray[17];
                architectNumber = toArray[18];
                architectEmail = toArray[19];
                architectAddress = toArray[20];


                /*
                View all the current projects in the text file
                 */
                if (whatToView == 1) {
                    output = toString(projectNumber, projectName, buildingType, buildingAddress, erfNumber,
                            totalProjectCost, totalPaidToDate, deadline, projectCompleted, customerName, customerNumber,
                            customerEmail, customerAddress, contractorName, contractorNumber, contractorEmail,
                            contractorAddress, architectName, architectNumber, architectEmail, architectAddress);
                }

                /*
                View all the projects that are past there due date
                 */
                else if (whatToView == 2) {

                    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd MMMM yyyy", Locale.ENGLISH);
                    LocalDate date =  LocalDate.parse(deadline, formatter);
                    LocalDate now = LocalDate.now();

                    if (date.compareTo(now) < 0) {
                        output = toString(projectNumber, projectName, buildingType, buildingAddress, erfNumber,
                                totalProjectCost, totalPaidToDate, deadline, projectCompleted, customerName, customerNumber,
                                customerEmail, customerAddress, contractorName, contractorNumber, contractorEmail,
                                contractorAddress, architectName, architectNumber, architectEmail, architectAddress);
                    }
                }

                /*
                View all the project that has not being completed
                 */
                else if (whatToView == 3) {
                    if (projectCompleted.equals("no")) {
                        output = toString(projectNumber, projectName, buildingType, buildingAddress, erfNumber,
                                totalProjectCost, totalPaidToDate, deadline, projectCompleted, customerName, customerNumber,
                                customerEmail, customerAddress, contractorName, contractorNumber, contractorEmail,
                                contractorAddress, architectName, architectNumber, architectEmail, architectAddress);
                    }
                }
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
            System.out.println("Could not read the file!");
        }
        return output;
    }
}
