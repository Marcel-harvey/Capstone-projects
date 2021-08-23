// Thanks for the feedback, really helped me improve the program

import javax.swing.*;
import java.awt.*;
import java.io.*;
import java.time.LocalDate;
import java.util.Arrays;
import java.util.Scanner;

// Convert toTextFile to list not string

public class Poised {
    public static void main(String[] args) {

        // Instantiate the new objects
        Project newProject = new Project();
        Person contractor = new Person();
        Person architect = new Person();
        Person customer = new Person();

        // Created for the dialog boxes
        int choice = 100;
        int project = 100;
        int edit = 100;

        // Used do-while loop to make sure that at least 1 instance of loop is run
        do {
            try {
                choice = Integer.parseInt(JOptionPane.showInputDialog("""
                        Choose an option below:
                        1.  Projects
                        2.  View projects (needs to be completed, past due date)
                        3.  Finalize project
                        0.  Quit program"""));
            }
            catch (NumberFormatException e) {
                JOptionPane.showInputDialog("Please enter a valid number!");
            }
            catch (HeadlessException e) {
                e.printStackTrace();
            }

            if (choice == 1) {
                try {
                    project = Integer.parseInt(JOptionPane.showInputDialog("""
                            What do you want to do? :
                            1.  Capture new project details
                            2.  Edit a current project
                            3.  Mark project as completed
                            4.  Back"""));
                }
                catch (NumberFormatException e) {
                    JOptionPane.showInputDialog("Please enter a valid number!");
                }
                catch (HeadlessException e) {
                    e.printStackTrace();
                }

                if (project == 1) {
                    /*
                     Ask the user to enter all the information about the project and the information of the
                     customer, architect and contractor that is working on the project.
                     All this information will be saved in a text file in 1 line
                    */
                    boolean flag = true;

                    try {
                        /*
                         Using 'PersonQuestions' and 'ProjectQuestions' classes to ask appropriate questions to fill
                         in data
                         Using 'Person' objects
                         Contractor
                        */
                        new PersonQuestions(contractor);

                        // Architect
                        new PersonQuestions(architect);

                        // Customer
                        new PersonQuestions(customer);


                        // Project
                        new ProjectQuestions(newProject, customer);
                    }
                    catch (HeadlessException e) {
                        JOptionPane.showInputDialog("Please enter correct values!");
                        flag = false;
                    }
                    catch (NumberFormatException e) {
                        e.printStackTrace();
                        flag = false;
                    }

                    // Get the stored information using getter
                    // order is project, customer, contractor and then architect
                    String toTextFile = newProject.getProjectDetails()+ ", no" +customer.getPersonDetails()
                            + contractor.getPersonDetails() + architect.getPersonDetails() +"\n";

                    // Writes the variable 'toTextFile' to the text file
                    if(flag) {
                        try {
                            BufferedWriter out = new BufferedWriter(new FileWriter("Project_Details.txt", true));
                            out.write(toTextFile);
                            out.close();
                        } catch (IOException e) {
                            System.out.println("Could not save to text file!");
                        }
                    }
                }

                else if (project == 2) {
                    try {
                        edit = Integer.parseInt(JOptionPane.showInputDialog("""
                                What do you want to edit or change?
                                1.  Due date
                                2.  Fee paid to date
                                3.  Contractor contact details
                                4.  Customer contact details
                                5.  Architect contact details"""));
                    }
                    catch (NumberFormatException e) {
                        System.out.println("Please enter a valid number!");
                    }
                    catch (HeadlessException e) {
                        e.printStackTrace();
                    }

                    if (edit == 1) {

                        int refNumber;
                        String newDeadline;

                        //  Ask the user the appropriate questions
                        refNumber = Integer.parseInt(JOptionPane.showInputDialog("""
                                Please enter the project number of the project you want to edit:"""));

                        newDeadline = JOptionPane.showInputDialog("""
                                What do you want to make the new deadline?""");

                        WriteToFile writeToFile = new WriteToFile(0,7, refNumber, newDeadline);

                    }


                    else if (edit == 2) {
                        int refNumber;
                        double newFeePaidDouble;

                        refNumber = Integer.parseInt(JOptionPane.showInputDialog("""
                                Please enter the project number of the project you want to edit:"""));

                        newFeePaidDouble = Integer.parseInt(JOptionPane.showInputDialog("""
                                What is the updated fee paid to date?"""));

                        // Cast from double to String for the method
                        String newFeePaid = String.valueOf(newFeePaidDouble);

                        WriteToFile writeToFile = new WriteToFile(0,6, refNumber, newFeePaid);
                    }


                    else if (edit == 3) {
                        // Person details
                        int refNumber;
                        int newNumberInt;

                        refNumber = Integer.parseInt(JOptionPane.showInputDialog("""
                                What is the project number that the contractor is working on?"""));

                        newNumberInt = Integer.parseInt(JOptionPane.showInputDialog("""
                                Enter the new number"""));
                        // Cast the number to a string before passing as an argument
                        String newNumber = Integer.toString(newNumberInt);

                        WriteToFile writeToFile = new WriteToFile(0,14, refNumber, newNumber);
                    }

                    else if (edit == 4) {
                        // Customer details
                        int refNumber;
                        int newNumberInt;

                        refNumber = Integer.parseInt(JOptionPane.showInputDialog("""
                                What is the project number of the customers project?"""));

                        newNumberInt = Integer.parseInt(JOptionPane.showInputDialog("""
                                Enter the new number"""));
                        // Cast the number to a string before passing as an argument
                        String newNumber = Integer.toString(newNumberInt);

                        WriteToFile writeToFile = new WriteToFile(0,10, refNumber, newNumber);
                    }

                    else if (edit == 5) {
                        // Architect details
                        int refNumber;
                        int newNumberInt;

                        refNumber = Integer.parseInt(JOptionPane.showInputDialog("""
                                What is the project number that the architect is working on?"""));

                        newNumberInt = Integer.parseInt(JOptionPane.showInputDialog("""
                                Enter the new number"""));
                        // Cast the number to a string before passing as an argument
                        String newNumber = Integer.toString(newNumberInt);

                        WriteToFile writeToFile = new WriteToFile(0,18, refNumber, newNumber);
                    }
                }

                else if (project == 3) {

                    int refNumber = Integer.parseInt(JOptionPane.showInputDialog
                            ("What is the project number of the project you want to mark as complete"));

                    WriteToFile writeToFile = new WriteToFile(0, 8, refNumber, "yes");
                }

                else if (project == 4) {
                    choice = 100;
                }
            }       // end of if statement choice 1


            else if (choice == 2) {
                // View projects, past due date, needs to be completed
                int whatToView = Integer.parseInt(JOptionPane.showInputDialog("""
                        Enter a number to choose what to view:
                        1.  View all projects
                        2.  View projects past due date
                        3.  View uncompleted projects
                        4.  Back"""));

                // View all
                if (whatToView == 1) {
                    // View all projects
                    ReadFile newRead = new ReadFile();
                    newRead.readFile(whatToView);
                }

                else if (whatToView == 2) {
                    // View overdue
                    ReadFile newRead = new ReadFile();
                    newRead.readFile(whatToView);
                }

                else if(whatToView == 3) {
                    // View uncompleted
                    ReadFile newRead = new ReadFile();
                    newRead.readFile(whatToView);
                }

            }       // end of if statement choice 2

            else if (choice == 3) {
                try {
                    // Ask the user for the project number to finalise that project
                    int refNumber = Integer.parseInt
                            (JOptionPane.showInputDialog("What is the project number of the project you want to finalize?"));

                    Scanner sc = new Scanner(new File("Project_Details.txt")).useDelimiter("\n");

                    double paidToDate;
                    double totalToPay;
                    int toCheck;
                    String projectName;
                    String customerName;
                    int customerContact;

                    /*
                     Reads the file line for line and splits it to an array to work with the data using indexing
                     Sliced the appropriate indexes for using in sting
                    */
                    while (sc.hasNextLine()){
                        String readFile = sc.nextLine();
                        String[] toArray = readFile.split(", ");
                        toCheck = Integer.parseInt(toArray[0]);
                        projectName = toArray[1];
                        customerName = toArray[9];
                        customerContact = Integer.parseInt(toArray[10]);
                        paidToDate = Double.parseDouble(toArray[5]);
                        totalToPay = Double.parseDouble(toArray[6]);

                        // Check if the project number the user gave matches with 1 of the project numbers in the file
                        if(toCheck == refNumber) {

                            /*
                            If the user still owes money the program will generate an invoice and save it to 'Invoice.txt'
                            The program will not append, so that there is always a new invoice to print
                             */
                            if (paidToDate != totalToPay) {
                                double whatToPay = paidToDate - totalToPay;
                                String invoice = customerName + " on project " + projectName + ", " + refNumber +
                                        ", " + customerContact + " still needs to pay R" + whatToPay;

                                JOptionPane.showInputDialog(invoice);

                                try {
                                    BufferedWriter out = new BufferedWriter(new FileWriter("Invoice.txt", false));
                                    out.write(invoice);
                                    out.close();
                                }
                                catch (IOException e) {
                                    System.out.println("Could not save to text file!");
                                }

                            }
                            // If the customer owes nothing, no invoice will be generated
                            else {
                                JOptionPane.showInputDialog("No invoice needed, payments are up to date");
                            }

                            /*
                            Builds the string to save in the 'Completed_Projects.txt' file
                            Removes the brackets '[]'
                            Then writes to file
                             */
                            LocalDate now = LocalDate.now();
                            String toTextFile = "finalized at " + now + ", " + Arrays.toString(toArray).replace
                                    ("[", "").replace("]", "") +"\n";

                            try {
                                BufferedWriter out = new BufferedWriter(new FileWriter("Completed_Projects.txt", true));
                                out.write(toTextFile);
                                out.close();
                            }
                            catch (IOException e) {
                                System.out.println("Could not save to text file!");
                            }

                            JOptionPane.showInputDialog("Project is finalized, check text files");
                        }

                    }
                }
                catch (FileNotFoundException e) {
                    e.printStackTrace();
                }
            }       // end of if statement choice 3

            else if (choice == 0) {
                System.out.println("All information is stored in the text files");
            } // end of if statement choice 0
        }
        while (choice != 0);
    }
}

/*
 Recourses:
 https://stackoverflow.com/questions/20039980/java-replace-line-in-text-file - This was just to get an idee to what i
 want to do
 https://www.tutorialspoint.com/how-to-compare-two-dates-in-java
 https://stackoverflow.com/questions/4216745/java-string-to-date-conversion
*/
