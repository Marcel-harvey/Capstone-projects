
public class Project {
	
	// Attributes
	int projectNumber;
	String projectName;
	String buildingType;
	String buildingAddress;
	int erfNumber;
	double totalCost;
	double totalPaid;
	String deadline;
	
	
	// Methods
	public Project(int projectNumber, String projectName, String buildingType, String buildingAddress, int erfNumber, double totalCost,
			double totalPaid, String deadline) {
		this.projectNumber = projectNumber;
		this.projectName = projectName;
		this.buildingType = buildingType;
		this.buildingAddress = buildingAddress;
		this.erfNumber = erfNumber;
		this.totalCost = totalCost;
		this.totalPaid = totalPaid;
		this.deadline = deadline;
	}
	
	// toString method
	public String toString() {
		String output = "\nThe prject number is: " +projectNumber;
		output += "\nThe name of the project is: " +projectName;
		output += "\nThe type of building is: " +buildingType;
		output += "\nThe address of the building is: " +buildingAddress;
		output += "\nThe Erf number is: " +erfNumber;
		output += "\nThe total cost of the project is: R" +totalCost;
		output += "\nThe amount paid to date is: R" +totalPaid;
		output += "\nThe deadline of the project is: " +deadline;
		
		return output;
	}

}
