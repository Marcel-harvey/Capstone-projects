import javax.swing.*;

public class PersonQuestions {
    public PersonQuestions(Person type) {
        String contractorName = (JOptionPane.showInputDialog("What is the %s's name?", type));
        type.setName(contractorName);

        String contractorSurname = (JOptionPane.showInputDialog("What is the %s's surname?", type));
        type.setSurname(contractorSurname);

        int contractorNumber = Integer.parseInt(JOptionPane.showInputDialog("What is the %s number?", type));
        type.setNumber(contractorNumber);

        String contractorEmail = (JOptionPane.showInputDialog("What is the e-mail address of the %s?", type));
        type.setEmail(contractorEmail);

        String contractorAddress = (JOptionPane.showInputDialog("What is the physical address of the %s?", type));
        type.setAddress(contractorAddress);
    }
}
