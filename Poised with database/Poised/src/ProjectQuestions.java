import javax.swing.*;

public class ProjectQuestions {

    /*
     Created method to ask the user questions to fill in the data for each object
     The data then gets stored using setters
    */
    public ProjectQuestions(Project type, Person customer) {
        int projectNumber = Integer.parseInt(JOptionPane.showInputDialog("What is the project number?:"));
        type.setProjectNumber(projectNumber);

        String projectName = (JOptionPane.showInputDialog("What is the project name?:"));
        type.setProjectName(projectName);

        String buildingType = (JOptionPane.showInputDialog("What type of building is the project going to be?:"));
        type.setBuildingType(buildingType);

        String buildingAddress = (JOptionPane.showInputDialog("What is the address of the building?:"));
        type.setBuildingAddress(buildingAddress);

        int erfNumber = Integer.parseInt(JOptionPane.showInputDialog("What is the ERF number?:"));
        type.setErfNumber(erfNumber);

        double totalCost = Double.parseDouble(JOptionPane.showInputDialog("What is the total cost of the project?:"));
        type.setTotalCost(totalCost);

        double totalPaid = Double.parseDouble(JOptionPane.showInputDialog("What is the amount already paid by the customer?:"));
        type.setTotalPaid(totalPaid);

        String deadline = (JOptionPane.showInputDialog("When should the project be finished?:\nExample: 02 january 2022"));
        type.setDeadline(deadline);

        type.setProjectCompleted("no");

        /*
         If the variable 'projectName' is empty, the customers surname and the building type will be used as the project
         name
        */
        if (projectName.isEmpty()) {
            type.setProjectName(type.getBuildingType()+ " " +customer.getSurname());
        }
    }
}
