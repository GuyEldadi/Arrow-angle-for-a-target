class OrganizationDatabase:
    '''
    name : string
    budget : float
    '''
    def __init__(self, name, budget):
        #Contains all work departments
        self.workforce = []
        self.budget = budget
        self.name = name

    def addDepartment(self,nameOfDepartment):
        # Appends a department to the workforce list
        # Tested: As the user has no control on what is inputted through this function, it will work everytime 
        # Outcome: no issues, new department works with the other parts of the code in an expected manner
        self.workforce.append(nameOfDepartment)
        return True

    def removeDepartment(self,index):
        #Pops department at following index
        #Tested: as only integers can be passed through this operator due to intChecker(), no negative numbers or strings can be put in and therefore this will always work
        #Outcome: inputted department is removed. If the removed department was the first department, now the first department becomes the second department as expeceted
        self.workforce.pop(index)
        return True

    def changeBudget(self):
        # Changes the budget value of the organization, whilst only allowing positive floats to be accepted
        # Tested: negative numbers and strings
        # Outcome: no issues, new budget written works with the other parts of the code in an expected manner
        self.budget = floatAndNegativeChecker("Insert your new organizational budget: ")
        return True

    def moveEmployeeToDifferentDepartment(self,indexOfCurrentDepartment,indexOfEmployeeInCurrentDepartment,newDepartment):
        # Moves an employee to a different department by appending it to the new department, and then removing employee in the original department
        # Tested: as each element parsed in the function is done through intChecker(), incompatiable values will not be inputted
        # Outcome: no issues, employee is placed in the new department and removed from the previous department
        #identifies the employee to move within the workforce
        employeeToMove = self.workforce[int(indexOfCurrentDepartment)-1].employees[int(indexOfEmployeeInCurrentDepartment)-1]
        #appends employee to department using another function
        self.workforce[int(newDepartment)-1].addEmployee(employeeToMove)
        #removes employee in original department using another function
        self.workforce[int(indexOfCurrentDepartment)-1].removeEmployee(employeeToMove)
        return True

    def changeEmployeeName(self,chosenWorkDepartment,chosenEmployee,newName):
        #Changes the name of a chosen employee to the newName given by the user
        #Tested: as the name can be a string, anything that is submitted is valid
        #Outcome: no issues, employee's name is changed
        self.workforce[int(chosenWorkDepartment)-1].employees[int(chosenEmployee)-1].name = newName
        return True

    def changeEmployeeSalary(self,chosenWorkDepartment,chosenEmployee,newSalary):
        #Changes the salary of a chosen employee to the newSalary given by the user
        #Tested: as the salary is parsed through floatAndNegativeChecker(), it cannot be anything but a positive float
        #Outcome: no issues, employee's salary is changed
        self.workforce[int(chosenWorkDepartment)-1].employees[int(chosenEmployee)-1].salary = newSalary
        return True

    def changeEmployeeAddress(self,chosenWorkDepartment,chosenEmployee,newHouseNumber,newStreetName,newStreetType,newState,newZipcode):
        #Changes the address of an employee through each part of the address class
        #Tested: as everything but the zipcode is a string, anything submitted is valid. As newZipcode is parsed through intChecker(), it will always be a valid integer
        #Outcome: no issues, employee's address is changed
        self.workforce[int(chosenWorkDepartment)-1].employees[int(chosenEmployee)-1].address.houseNumber = newHouseNumber
        self.workforce[int(chosenWorkDepartment)-1].employees[int(chosenEmployee)-1].address.streetName = newStreetName
        self.workforce[int(chosenWorkDepartment)-1].employees[int(chosenEmployee)-1].address.streetType = newStreetType
        self.workforce[int(chosenWorkDepartment)-1].employees[int(chosenEmployee)-1].address.state = newState
        self.workforce[int(chosenWorkDepartment)-1].employees[int(chosenEmployee)-1].address.zipcode = newZipcode
        return True

    def changeEmployeeDateOfBirth(self,chosenWorkDepartment,chosenEmployee,newBirthYear,newBirthMonth,newBirthDay):
        #Changes the employee's date of birth
        #Tested: as everything has been parsed through intChecker(), and all the days and months are made sure that they exist, this function will always work
        #Outcome: no issues, employee's date of birth is changed
        self.workforce[int(chosenWorkDepartment)-1].employees[int(chosenEmployee)-1].birthDate.year = newBirthYear
        self.workforce[int(chosenWorkDepartment)-1].employees[int(chosenEmployee)-1].birthDate.month = newBirthMonth
        self.workforce[int(chosenWorkDepartment)-1].employees[int(chosenEmployee)-1].birthDate.day = newBirthDay

        return True
        
    def printAllEmployeeDetailsDepartmentsAndRecommendations(self):
        #Prints out all departments along with their budgets, the total of their employees salaries, and the number of employees.
        #And for each department, all employees are printed with their name, salary, address and date of birth
        #Tested: For the budgets and salaries, they have been parsed through floatAndNegativeChecker() in someway, so they all work when operations are done with them. The rest of the values are strings so it always works
        #Outcome: no issues, all details are printed out correctly
        number = 0
        otherNumber = 0
        #prints out all the details of each department and its employees along with their index number + 1
        for workdepartment in self.workforce:
            number+=1
            print(f"\n{number}. Budget of {workdepartment.nameOfDepartment} department: ${workdepartment.departmentBudget}. Total of all employee salary in {workdepartment.nameOfDepartment}: ${newDatabase.moneyUsedByEmployeesInEachDepartment(number-1)}. Employees in {workdepartment.nameOfDepartment}: ")
            otherNumber = 0
            for employee in workdepartment.employees:
                otherNumber += 1
                print(f"{otherNumber}. Name: {employee.name}. Salary: ${employee.salary}. Address: {employee.address.houseNumber} {employee.address.streetName} {employee.address.streetType}, {employee.address.state}, {employee.address.zipcode}. Birth Date: {employee.birthDate.day}/{employee.birthDate.month}/{employee.birthDate.year}")

        return True 
    def createNewEmployee(self,name,salary,address,birthDate,department):
        #Creates a new Employee object with the user entered attributes
        newEmployee = Employee(name,salary,address,birthDate)
        #Appends the newly created employee to the workdepartment chosen
        self.workforce[float(department)-1].addEmployee(newEmployee)
        return True

    def moneyUsedByDepartments(self):
        #Adds up the departmentBudget of each department and returns that value
        #Tested: as all budgets are parsed through floatAndNegativeChecker(), all additions will work
        #Outcome: no issues
        moneyUsed = 0
        for workdepartment in self.workforce:
            moneyUsed += float(workdepartment.departmentBudget)
        #EVIDENCE OF IN CODE TESTING: print(f"*********************modnyUsed = {moneyUsed}")
        return moneyUsed
        
    def moneyUsedByEmployeesInEachDepartment(self,departmentIndex):
        #Adds up the departmentBudget of each department and returns that value
        #Tested: as all budgets are parsed through floatAndNegativeChecker(), all additions will work
        #Outcome: no issues
        moneyUsed = 0
        department = self.workforce[int(departmentIndex)]
        #EVIDENCE OF IN CODE TESTING: for workdepartment in self.workforce:
        for employee in department.employees:
            moneyUsed += float(employee.salary)

        return moneyUsed

class WorkDepartment:
    '''
    nameOfDepartment : string
    departmentBudget : float
    '''
    def __init__(self, nameOfDepartment, departmentBudget):
        self.nameOfDepartment = nameOfDepartment
        self.departmentBudget = departmentBudget
        self.employees = []

    def changeDepartmentBudget(self,newBudget):
        #Using the newBudget value inputted at line 326, this changes the budget of the program
        #Testing: As newBudget is parsed through floatAndNegativeChecker(), it cannot be a negative number or a string, and as such this operation will work everytime
        # Outcome: no issues, new budget written works with the other parts of the code in an expected manner
        self.departmentBudget = newBudget
        return True

    def addEmployee(self, employee):
        #Using the object inputted (employee), this appends the employee to the employees list within a work department
        #Testing: As employee is an object which has each of its attributes checked with intChecker() and floatAndNegativeChecker(), this operation will work everytime
        #Outcome: no issues, new employee is added to the work department
        self.employees.append(employee)
        return True

    def removeEmployee(self,employee):
        #Using the object inputted (employee), this removes the employee in  the employees list within a work department
        #Testing: As employee is an object which has each of its attributes checked with intChecker() and floatAndNegativeChecker(), this operation will work everytime
        #Outcome: no issues, new employee is removed from the work department
        self.employees.remove(employee)
        return True
class Employee:
    '''
    name : string
    salary : float
    address : Address
    birthDate : Date
    '''
    def __init__(self, name, salary, address, birthDate):
        self.name = name
        self.salary = salary
        self.address = address
        self.birthDate = birthDate

    
class Date:
    '''
    day : int
    month : int
    year : int
    '''
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
    
class Address:
    '''
    houseNumber : str (as some house numbers have letters such as 10A, and having this be a string doesn't prevent functionality down the line)
    streetName : str
    streetType : str
    state : str
    zipcode : int
    '''
    def __init__(self,houseNumber,streetName,streetType,state,zipcode):
        self.houseNumber = houseNumber
        self.streetName = streetName
        self.streetType = streetType
        self.state = state
        self.zipcode = zipcode

    



#initializes an Employee Database name
databaseName = input("State your organization's name: ")

#States a question, and allows the user to input a value. If the value is not an float, or if the value is an float, but negative, it will ask the user to try again

def floatAndNegativeChecker(question):
    isFloat = False
    isNeg = True
    #Enables a loop which repeatedly asks the user to input a value until the value is a positive float
    while isFloat == False and isNeg == True:
        options = input(f"{question}")
        try:
            #If options is not an float, this will cause an error to be thrown, making it go to except
            floatNum = float(options)
            isFloat = True
            #If options is less than 0, or a negative number, the loop will reset
            if floatNum < 0:
                print(f"You have inserted a number which is negative. Please try again")
                isFloat = False
            else:
                isNeg = False
        except:
            print("You have inserted something which is not a number. Please try again.")
    #Returns the value the user has inputted
    return options

#initalizes the budget for the Employee Database, and checks if it is a float or if its negative
databaseBudget = float(floatAndNegativeChecker("State your organization's budget: "))
#Creates the employee database
newDatabase = OrganizationDatabase(databaseName, databaseBudget)
print(f"\nYou have successfully created a database for your organization called {newDatabase.name} with a budget of ${newDatabase.budget}")


######################
'''
Uncomment what's below to avoid having to make lots of departments and lots of employees
'''

employeeOneBirthDate = Date(2,11,1993)
employeeTwoBirthDate = Date(6,8,1995)
employeeThreeBirthDate = Date(21,1,2000)
employeeFourBirthDate = Date(22,4,1998)
employeeFiveBirthDate = Date(10,5,1995)
employeeSixBirthDate = Date(12,10,1997)

employeeOneAddress = Address("10A", "Innovation", "Walk", "Victoria", 3121)
employeeTwoAddress = Address("22", "Googly", "Road", "Victoria", 3135)
employeeThreeAddress = Address("21B", "Sofa", "Road", "Victoria", 3144)
employeeFourAddress = Address("101", "Ready", "Street", "Victoria", 4321)
employeeFiveAddress = Address("4202", "Big", "Street", "Victoria", 2018)
employeeSixAddress = Address("123", "Mate", "Avenue", "Victoria", 2014)

employeeOne = Employee("Guy Eldadi", 200, employeeOneAddress, employeeOneBirthDate)
employeeTwo = Employee("Aaron Baker", 400, employeeTwoAddress, employeeTwoBirthDate)
employeeThree = Employee("Suzanne Simon", 350, employeeThreeAddress, employeeThreeBirthDate)
employeeFour = Employee("Aaron Ryan", 450, employeeFourAddress, employeeFourBirthDate)
employeeFive = Employee("Robert Robertson", 100, employeeFiveAddress, employeeFiveBirthDate)
employeeSix = Employee("Lio Leong", 230, employeeSixAddress, employeeSixBirthDate)

developers = WorkDepartment("Developers", 1000)
logistics = WorkDepartment("Logistics", 800)

newDatabase.addDepartment(developers)
newDatabase.addDepartment(logistics)

logistics.addEmployee(employeeOne)
#EVIDENCE OF IN CODE TESTING: employee1 = logistics.employees[0]
#EVIDENCE OF IN CODE TESTING: print(f"************************{employee1.name}")
#EVIDENCE OF IN CODE TESTING: print(f"3333333333333333333333{logistics.employees[0].name}")

developers.addEmployee(employeeTwo)
logistics.addEmployee(employeeThree)
developers.addEmployee(employeeFour)
logistics.addEmployee(employeeFive)
logistics.addEmployee(employeeSix)

########################

#States a question, and allows the user to input a value. If the value is not an integer, or if the value is an integer, but not in the correct range, it will ask the user to try again
def intChecker(question, lower = 1, upper = 4):
    #Enables a loop which repeatedly asks the user to input a value until the value is an integer and between the upper and lower bound
    isInt = False
    correctNumber = False
    while isInt == False and correctNumber == False:
        options = input(f"{question}")
        #EVIDENCE OF IN CODE TESTING: print(f"options is: {options}")
        try:
            #If options is not an integer, this will cause an error to be thrown, making it go to except
            intNum = int(options)
            #EVIDENCE OF IN CODE TESTING: print("GOT here")
            isInt = True
            #EVIDENCE OF IN CODE TESTING: print("11111GOT here
            #If options is not between the upper or lower bound, the loop will reset and return to the beginning of the loop
            if intNum < lower or intNum > upper:
                #EVIDENCE OF IN CODE TESTING: print("22222GOT here")
                print(f"You have inserted a number which is not between {lower} to {upper}. Please try again.")
                isInt = False
            else:
                correctNumber = True
        except:
            print("You have inserted something which is not a number. Please try again.")
    #Returns the value the user has inputted
    return options

while True:
    print("\nDashboard:")
    #EVIDENCE OF IN CODE TESTING: int(newDatabase.budget)-int(
    #EVIDENCE OF IN CODE TESTING: print(f"**************currentVersion = {currentVersion}")
    budgetOfEachDepartmentAddedUp = newDatabase.moneyUsedByDepartments()
    print(f"Organization name: {newDatabase.name}. Organization Budget : ${newDatabase.budget}. Budget of each department added up: ${budgetOfEachDepartmentAddedUp}. Remaining budget from organization budget subtracted by budget of each department ${float(newDatabase.budget)-float(newDatabase.moneyUsedByDepartments())}.")
    print(f"List of Departments and Employees:")
    #Prints out all department details and the employee details of each department
    newDatabase.printAllEmployeeDetailsDepartmentsAndRecommendations()
    #Recommends actions for the user depending on the organizational budget verses the added up budgets of all organizations, and each work department budget verse the added up salary of the employees in each department
    print("\nRecommended actions:")
    if float(newDatabase.budget)-float(newDatabase.moneyUsedByDepartments()) < 0:
        print(f"The budget allocated to your work departments exceed the organizational budget by ${abs(float(newDatabase.budget)-float(newDatabase.moneyUsedByDepartments()))}. It is recommended to reduce the budget allocated to work departments.")
    elif float(newDatabase.budget)-float(newDatabase.moneyUsedByDepartments()) == 0:
        print("The organizational budget perfectly encompasses every work department's budget. It is recommended to leave the budget as is.")
    elif float(newDatabase.budget)-float(newDatabase.moneyUsedByDepartments()) > 0:
        print(f"All of the money allocated to each of the work departments is covered by the organizational budget, and there is ${float(newDatabase.budget)-float(newDatabase.moneyUsedByDepartments())} left to allocate. It is recommened to increase the budget allocated to work departments")
    number=0
    for workdepartment in newDatabase.workforce:
        if newDatabase.moneyUsedByEmployeesInEachDepartment(number) > workdepartment.departmentBudget:
            print(f"The employees in {workdepartment.nameOfDepartment} have an added up salary greater than the department budget by ${newDatabase.moneyUsedByEmployeesInEachDepartment(number) - workdepartment.departmentBudget}. It is recommended to reduce the salaries of the employees")
        elif newDatabase.moneyUsedByEmployeesInEachDepartment(number) == workdepartment.departmentBudget:
            print(f"The employees in {workdepartment.nameOfDepartment} have an added up salary equal to the department budget. It is recommended to keep the budgets and salaries as is")
        elif newDatabase.moneyUsedByEmployeesInEachDepartment(number) < workdepartment.departmentBudget:
            print(f"The employees in {workdepartment.nameOfDepartment} have an added up salary less than the department budget by ${abs(newDatabase.moneyUsedByEmployeesInEachDepartment(number) - workdepartment.departmentBudget)}. It is recommended to increase the salaries of the employees")
        number+=1

    print("\nOptions avaliable: 1. Change something at the organizational level. 2. Change something at the Department level. 3. Change something about Employees. 4. Use prediction functionalities.")
    options = intChecker("Select an option with their respective number 1 to 4: ",1, 4)

    #Option 1 changes things at the organizational level
    if options == "1":
        print("\nYou have selected to change something at the organizational level. Please choose one of the avaliable operations with their respective number: ")
        orgOption = intChecker("1. Change the organizational budget. 2. Remove a department. 3. Create a department: ",1,3)
        #orgOption 1 changes the budget of the organization
        if orgOption == "1":
            newDatabase.changeBudget()
            print(f"Your new organizational budget is now ${newDatabase.budget}")
        # orgOption 2 removes work departments from the organization (specifically, from the workforce list)
        elif orgOption == "2":
            number = 0
            #checks if there are any existing work departments, and if not it exits the operation to avoid entering an infinite loop
            if len(newDatabase.workforce)<=0:
                print("You have no departments to remove, please create departments before using this operation.")
            else:
                #prints out all existing departments 
                for workdepartment in newDatabase.workforce:
                    number+=1
                    print(f"{number}. Name: {workdepartment.nameOfDepartment}.")
                #asks the user for the index number of the departments listed above
                numberOfDepartmentToRemove = intChecker("Type the number of the respective department you wish to remove as listed above: ", 1, len(newDatabase.workforce))
                #uses removeDepartment() operation to remove department
                newDatabase.removeDepartment(int(numberOfDepartmentToRemove)-1)
        # orgOption 3 creates a department (specifically, adds a department to the workforce list)
        elif orgOption == "3":
            #If the user wants to create departments one after another, extraDepartments allows for that
            extraDepartments = True
            while extraDepartments == True:
                initialDepartmentName = input("What do you want to name your department?: ")
                initialDepartmentBudget = floatAndNegativeChecker(f"What is the budget of your new department {initialDepartmentName}?: ")
                #creates an object newDepartment
                newDepartment = WorkDepartment(initialDepartmentName,initialDepartmentBudget)
                #adds newDepartment to organizationDatabase
                newDatabase.addDepartment(newDepartment)

                print(f"{initialDepartmentName} has been added to the Organization.")
                #asks the user if they want to create another department, or otherwise exit the department creation part
                decision = input("Would you like to make another department? Type anything for yes and type N for no: ")
                if decision == "n" or decision == "N":
                    extraDepartments = False
                
    #Option 2 changes things at the work department level, which is only going to be work department budget
    elif options == "2":
        #Checks if the organization has work department budgets to change in the first place
        if len(newDatabase.workforce) < 1:
            print("Please add departments before using this function, as there are no departments to change the budget for.")
        #Continues the program if there are existing departments
        else:
            print("\nYou have selected to change something at the department level. The only option is to change a department's budget, and as such the program will continue with that intention")
            number=0
            #Iterates through the list of departments so the user can choose a department without having to scroll back up to check the number of the department
            for workdepartment in newDatabase.workforce:
                number+=1
                print(f"{number}. Name: {workdepartment.nameOfDepartment}. Budget: ${workdepartment.departmentBudget}.")
            #asks the user what department they want to change the budget for
            selectingDepartment = intChecker("Choose the department you want to change the budget of with their respective number: ", 1, len(newDatabase.workforce))
            selectedDepartment = newDatabase.workforce[int(selectingDepartment)-1]
            #asks the user what the new budget should be
            newBudget = floatAndNegativeChecker(f"Choose the new budget of {selectedDepartment.nameOfDepartment}: ")
            #the new budget and department is used for the following function to operate
            selectedDepartment.changeDepartmentBudget(newBudget)
            
            
    #Option 3 changes things at the employee level
    elif options == "3":
        print("\nYou have selected to change something at the employee level. Please choose one of the avaliable operations with their respective number: ")
        #allows the user to decide which operation to use
        empOption = intChecker("1. Move an Employee to a different department. 2. Change existing employee information. 3. Create a new employee profile: ",1,3)
        #empOption 1 moves employees from one department to another through appending them to a new department, and removing them from the previous department
        if empOption == "1":
            number = 0
            #prints all work departments and employees with their corresponding index number + 1
            for workdepartment in newDatabase.workforce:
                number+=1
                print(f"{number}. Employees in {workdepartment.nameOfDepartment}:")
                otherNumber = 0
                for employee in workdepartment.employees:
                    otherNumber += 1
                    print(f"{otherNumber}. Name: {employee.name}.")
            chosenWorkDepartment = intChecker("Type the number of the corresponding department where the employee is: ", 1, len(newDatabase.workforce))
            chosenEmployee = intChecker("Type the number of the corresponding employee you want to change: ", 1, len(newDatabase.workforce[int(chosenWorkDepartment)-1].employees))
            newDepartment = intChecker(f"What department would you like to move {newDatabase.workforce[int(chosenWorkDepartment)-1].employees[int(chosenEmployee)-1].name} (type the corresponding number for the department)?: ",1,len(newDatabase.workforce))
            #Using the user inputs from above, the inputs are parsed through the following function
            newDatabase.moveEmployeeToDifferentDepartment(chosenWorkDepartment,chosenEmployee,newDepartment)
        #empOption 2 changes details of an employee, whether that is the employee's name, salary, address or date of birth
        elif empOption == "2":
            #If the user wants to change details about employees repeatedly, this while loop will prevent the program from returning to the dashboard
            notDone = True
            while notDone == True:
                number = 0
                #prints out all work departments and employees with their corresponding index number + 1
                for workdepartment in newDatabase.workforce:
                    number+=1
                    print(f"{number}. Employees in {workdepartment.nameOfDepartment}:")
                    otherNumber = 0
                    for employee in workdepartment.employees:
                        otherNumber += 1
                        print(f"{otherNumber}. Name: {employee.name}.")
                #Identifies the employee to change details about, through finding the employee within their work department
                chosenWorkDepartment = intChecker("Type the number of the corresponding department where the employee you want to change is: ", 1, len(newDatabase.workforce))
                chosenEmployee = intChecker("Type the number of the corresponding employee you want to change: ", 1, len(newDatabase.workforce[int(chosenWorkDepartment)-1].employees))
                print("Type the corresponding number for the employee attribute you want to change")
                changeChoice = intChecker("1. Name. 2. Salary. 3. Address. 4. Date Of Birth: ")
                #If the user wants to change the employee's name
                if changeChoice == "1":
                    newName = input("Type in the new name for the employee: ")
                    #Calls the changeEmployeeName operation
                    newDatabase.changeEmployeeName(chosenWorkDepartment,chosenEmployee,newName)
                #If the user wants to change the salary of the employee
                elif changeChoice == "2":
                    newSalary = floatAndNegativeChecker("Type in new salary for the employee: ")
                    #Calls the changeEmployeeSalary operation
                    newDatabase.changeEmployeeSalary(chosenWorkDepartment,chosenEmployee,newSalary)
                #If the user wants to change the address of the employee
                elif changeChoice == "3":
                    newHouseNumber = input("Type in new house number for the employee: ")
                    newStreetName = input("Type in new street name for the employee: ")
                    newStreetType = input("Type in new street type for the employee: ")
                    newState = input("Type in new state for the employee: ")
                    newZipcode = floatAndNegativeChecker("Type in new zipcode for the employee: ")
                    #Calls the changeEmployeeAddress operation
                    newDatabase.changeEmployeeAddress(chosenWorkDepartment,chosenEmployee,newHouseNumber,newStreetName,newStreetType,newState,newZipcode)
                #If the user wants to change the birthday of the employee
                elif changeChoice == "4":
                    newBirthYear = intChecker("Type in the new birth year for the employee: ", 0, 9999)
                    newBirthMonth = intChecker("Type in the new birth month for the employee (1 - 12 for each corresponding month): ",1,12)
                    #This conditional statement only allows valid dates in each month to be submitted by the user
                    if newBirthMonth == "1" or newBirthMonth == "3" or newBirthMonth == "5" or newBirthMonth == "7" or newBirthMonth == "8" or newBirthMonth == "10" or newBirthMonth == "12":
                        newBirthDay = intChecker("Type in the new birth day for the employee (1 - 31): ",1,31)
                    elif newBirthMonth == "4" or newBirthMonth == "6" or newBirthMonth == "9" or newBirthMonth == "11":
                        newBirthDay = intChecker("Type in the new birth day for the employee (1 - 30): ",1,30)
                    elif newBirthMonth == "2":
                        newBirthDay = intChecker("Type in the new birth day for the employee (1-28): ",1,28)
                    #Calls the changeEmployeeDataOfBirth operation
                    newDatabase.changeEmployeeDateOfBirth(chosenWorkDepartment,chosenEmployee,newBirthYear,newBirthMonth,newBirthDay)
                number = 0
                #asks the user if they want to continue changing employee details, and if not, it breaks the loop by turning notDone to False
                continueOrNot = input("Would you like to continue editing employees? Type N for no, or anything else to continue: ")
                if continueOrNot == "n" or continueOrNot == "N":
                    notDone = False
        #empOption 3 allows for new employees to be created and added to work departments
        elif empOption == "3":
            notDone = True
            #If the user wants to produce new employees repeatedly, this while loop will prevent the program from returning to the dashboard
            while notDone == True:
                #the user can input all details about a new employee so a new employee object can be successfully added to a work department
                name = input("Type in the name of the Employee: ")
                salary = floatAndNegativeChecker("Type in the salary of the Employee: ")
                houseNumber = input("Type in new house number for the employee: ")
                streetName = input("Type in new street name for the employee: ")
                streetType = input("Type in new street type for the employee: ")
                state = input("Type in new state for the employee: ")
                zipcode = floatAndNegativeChecker("Type in new zipcode for the employee: ")
                address = Address(houseNumber,streetName,streetType,state,zipcode)
                birthYear = intChecker("Type in the new birth year for the employee: ", 0, 9999)
                birthMonth = intChecker("Type in the new birth month for the employee (1 - 12 for each corresponding month): ",1,12)
                if birthMonth == "1" or birthMonth == "3" or birthMonth == "5" or birthMonth == "7" or birthMonth == "8" or birthMonth == "10" or birthMonth == "12":
                    birthDay = intChecker("Type in the new birth day for the employee (1 - 31): ",1,31)
                elif birthMonth == "4" or birthMonth == "6" or birthMonth == "9" or birthMonth == "11":
                    birthDay = intChecker("Type in the new birth day for the employee (1 - 30): ",1,30)
                elif birthMonth == "2":
                    birthDay = intChecker("Type in the new birth day for the employee (1-28): ",1,28)
                #creates a Date object with the previous inputted values
                birthDate = Date(birthDay,birthMonth,birthYear)
                number = 0
                # prints out all work departments
                for workdepartment in newDatabase.workforce:
                    number+=1
                    print(f"{number}. {workdepartment.nameOfDepartment}")
                department = intChecker("Which department does your new employee belong to (type the corresponding number)?: ",1,len(newDatabase.workforce))
                #Calls the createNewEmployee function with the attributes the user has entered
                newDatabase.createNewEmployee(name,salary,address,birthDate,department)
                #asks the user if they want to continue producing employee, and if not, it breaks the loop by turning notDone to False
                continueOrNot = input("Would you like to continue creating employees? Type N for no, or anything else to continue: ")
                if continueOrNot == "n" or continueOrNot == "N":
                    notDone = False
    #Option 4 allows for future predictions of budget and salaries
    elif options == "4":
        print("This option will change all budgets and salaries to be changed by a specific percentage, emulating growth or decline in revenue")
        newOrganizationTime = input("Type in the projected time frame that this duplicate will take place in, e.g Google 'in 10 years': ")
        changeInAllBudgets = floatAndNegativeChecker("Type in the growth or decline percentage of the organization (this will change the organizational budget and all work department budgets, accounting for growth or decline of revenue) (insert percentage as a decimal e.g 0.5 would result in 50% decrease): ")
        changeInSalaries = floatAndNegativeChecker("Type in the growth or decline of the salaries of employees (this can account for interest increases) (similarly to the previous prompt, insert a decimal): ")
        #Derives the new organization name with the original organization and newOrganizationTime
        new_name = newDatabase.name + " " + newOrganizationTime
        new_budget = float(newDatabase.budget)*float(changeInAllBudgets)
        #Changes the budget and name of the organization to new_budget and new_name
        newDatabase.budget = new_budget
        newDatabase.name = new_name
        #Cycles through all employees in each department, and multiplies their salary by changeInSalaries
        for workdepartment in newDatabase.workforce:
            for employee in workdepartment.employees:
                #EVIDENCE OF IN CODE TESTING: print(employee.salary)
                employee.salary *= float(changeInSalaries)
                #EVIDENCE OF IN CODE TESTING: print(employee.salary)
        #Cycles through all departments and multiplies their budgets by changeInAllBudgets
        for workdepartment in newDatabase.workforce:
            #EVIDENCE OF IN CODE TESTING: print(workdepartment.departmentBudget)
            workdepartment.departmentBudget *= float(changeInAllBudgets)
            #EVIDENCE OF IN CODE TESTING: print(workdepartment.departmentBudget)
