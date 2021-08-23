public class Person {

    private String name;
    private String surname;
    private int number;
    private String email;
    private String address;

    public void setName(String newName) {
        name = newName;
    }

    public void setNumber(int newNumber) {
        number = newNumber;
    }

    public void setEmail(String newEmail) {
        email = newEmail;
    }

    public void setAddress(String newAddress) {
        address = newAddress;
    }

    public void setSurname(String newSurname) { surname = newSurname;}

    public String getSurname() {
        return surname;
    }


    public String getPersonDetails() {
        return ", "+name+ ", " +number+ ", " +email+ ", " +address;
    }

}
