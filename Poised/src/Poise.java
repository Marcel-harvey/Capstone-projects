import javax.swing.*;

public class Poise {
	
	public static void main(String[] args) {
		
		// Created blank variables for the user to enter in, this can help to edit it to
		int projectNumber = 0;
		String projectName = "";
		String buildingType = "";
		String buildingAddress = "";
		int erfNumber = 0;
		double totalCost = 0.0;
		double totalPaid = 0.0;
		String deadline = "";
		
		// Created my own contractor with some details
		String personName = "";
		String personNumber = "";
		String personEmail = "";
		String personAddress = "";
		
		
		// Made a while loop so that the program can keep running until the user wants to exit, by pressing 0
		int choice;
		do {
			// Created an option bar for the user to choose from
			System.out.println( "Enter a number to choose an option:\n" );
			choice = Integer.parseInt( JOptionPane.showInputDialog("""
					1. Capture project details
					2. Edit project
					3. capture persons details
					4. Update persons details
					0. Quit program""") );
			
			// If the user entered 1
			// The user will be asked to answer a couple of questions with the details of the project
			// All the question will be shown on the dialog box
			// The inputs then gets saved in the variable names, to save as objects later
			if (choice == 1) {
				projectNumber = Integer.parseInt( JOptionPane.showInputDialog("What is the project number?:"));
				
				projectName = ( JOptionPane.showInputDialog("What is the project name?:"));
				
				buildingType = ( JOptionPane.showInputDialog("What type of building is the project going to be?:"));

				buildingAddress = ( JOptionPane.showInputDialog("What is the address of the building?:"));
				
				erfNumber = Integer.parseInt( JOptionPane.showInputDialog("What is the ERF number?:"));
				
				totalCost = Double.parseDouble( JOptionPane.showInputDialog("What is the total cost of the project?:"));
				
				totalPaid = Double.parseDouble( JOptionPane.showInputDialog("What is the amount already paid by the customer?:"));
				
				deadline = ( JOptionPane.showInputDialog("When should the project be finished?:"));
			}
			
			// If the user entered 2
			// The user gets asked what he wants to edit
			else if (choice == 2) {
				int edit = Integer.parseInt( JOptionPane.showInputDialog("""
						1. Due date
						2. Fee paid to date
						"""));
				
				// If the user entered 1
				// Asks the user what he wants to change the date to and changes the input
				if (edit == 1) {
					deadline = ( JOptionPane.showInputDialog("When should the project be finished?:"));
				}
				// If the user entered 2
				// Asks what the updated fee is and changes the variable to the input
				else if (edit == 2) {
					totalPaid = Double.parseDouble( JOptionPane.showInputDialog("What is the amount already paid by the customer?:"));
				}				
			}
			
			// If the user entered 3
			// The user gets asked a couple of questions about the details of the person
			// The question will be shown in the dialog box
			// Answers gets saved to the variable and later user
			else if (choice == 3) {
				personName = ( JOptionPane.showInputDialog("What is name of the person you want to register?:"));

				personNumber = ( JOptionPane.showInputDialog("What is the number of the person you want to register?:"));

				personEmail = ( JOptionPane.showInputDialog("What is the email of the person you want to register?:"));

				personAddress = ( JOptionPane.showInputDialog("What is the address of the person you want to register?:"));
			}

			else if (choice == 4) {
				personNumber = ( JOptionPane.showInputDialog("What is the new number of the person?:"));
			}
			else{
				System.out.println("There is no such option, please try again");
			}
			
		}
		while( choice != 0 );
		
		
		// Saves all the info as objects with the given variables as there values
		Project project1 = new Project(projectNumber, projectName, buildingType, buildingAddress, erfNumber, totalCost, totalPaid, deadline);
		Person contractor = new Person(personName, personNumber, personEmail, personAddress);
		
		// Displays all the information to the user after he exited the program
		System.out.println("Details for the Project:\n" +project1);
		System.out.println("Details for the Person:\n" +contractor);
	}
	

}
// This is about as good as i could think of, i did not understand the task clearly enough, what is required and so on
// Any feedback will be appreciated
