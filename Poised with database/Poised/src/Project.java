public class Project {

    private int projectNumber;
    private String projectName;
    private String buildingType;
    private String buildingAddress;
    private int erfNumber;
    private double totalCost;
    private double totalPaid;
    private String deadline;
    private String projectCompleted;


    public void setProjectNumber(int number) {
        projectNumber = number;
    }

    public void setProjectName(String name) {
        projectName = name;
    }


    public void setBuildingType(String type) {
        buildingType = type;
    }


    public void setBuildingAddress(String address) {
        buildingAddress =address;
    }
    public String getBuildingType() { return buildingType; }


    public void setErfNumber(int erf) {
        erfNumber = erf;
    }


    public void setTotalCost(double cost) {
        totalCost = cost;
    }


    public void setTotalPaid(double paid) {
        totalPaid = paid;
    }


    public void setDeadline(String lastDay) {
        // Made the first letter in the string a capital letter
        String firstLetter = lastDay.substring(0, 1);
        String restOfLetter = lastDay.substring(1);

        firstLetter = firstLetter.toUpperCase();

        String rebuildOfString = firstLetter + restOfLetter;

        deadline = rebuildOfString;
    }

    public void setProjectCompleted(String completed) { projectCompleted = completed; }

    public String getProjectDetails() {
        return projectNumber+ ", " +projectName+ ", " +buildingType+ ", " +buildingAddress+ ", " +erfNumber+ ", "
                +totalCost+ ", " +totalPaid+ ", " +deadline;
    }


}
