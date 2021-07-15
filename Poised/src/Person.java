public class Person {
	
	// Attributes
	String name;
	String number;
	String email;
	String address;
	
	
	// Methods
	public Person(String name, String number, String email, String address) {
		this.name = name;
		this.number = number;
		this.email = email;
		this.address = address;
	}
	
	public String getName() {return name;}
	
	
	// toString method
	public String toString() {
		String output = "\nName: " +name;
		output += "\nNumber: " +number;
		output += "\nE-mail: " +email;
		output += "\nAddress: " +address;
		
		return output;
	}

}
