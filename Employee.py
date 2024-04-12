

class Employee():
    """Python class to implement a basic version of a hotel employee.

    This Python class implements the basic functionalities of a hotel employee in a 
    simple hotel management system.

    Syntax
    ------
    obj = Employee(emp_id, name, position, salary)

    Parameters
    ----------
    [in] emp_id : int
        Unique identifier for the employee.
    [in] name : str
        Name of the employee.
    [in] position : str
        The job position of the employee (e.g., 'Receptionist', 'Housekeeper', 'Manager').
    [in] salary : float
        The salary of the employee.

    Returns
    -------
    obj : Employee
        Python object output parameter that represents an instance of the class Employee.

    Attributes
    ----------
    """
    #Here you start your code.

    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.assigned_tasks = []


    #getters y setters
    def get_emp_id(self):
        return self._emp_id

    def set_emp_id(self, emp_id):
        if isinstance(emp_id, int):
            self._emp_id = emp_id
        else:
            raise TypeError("El ID del empleado debe ser un número entero.")


    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("El nombre del empleado debe ser una cadena de texto.")


    def get_position(self):
        return self._position

    def set_position(self, position):
        if isinstance(position, str):
            self._position = position
        else:
            raise TypeError("La posición del empleado debe ser una cadena de texto.")
        
    
    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        if isinstance(salary, int):
            self._salary = salary
        else:
            raise TypeError("El salario del empleado debe ser un número entero.")


    def get_assigned_tasks(self):
        return self._assigned_tasks

    def set_assigned_tasks(self, tasks):
        if isinstance(tasks, list):
            self._assigned_tasks = tasks
        else:
            raise TypeError("Las tareas asignadas deben ser una lista.")


    #métodos necesarios para añadir/eliminar habitaciones y empleados
    def add_room(self, room):
        self.assigned_tasks.append(f"Añadir habitación {room.get_room_number()}")

    def remove_room(self, room):
        self.assigned_tasks.append(f"Eliminar habitación {room.get_room_number()}")

    def add_employee(self, employee):
        self.assigned_tasks.append(f"Añadir empleado {employee.name}")

    def remove_employee(self, employee):
        self.assigned_tasks.append(f"Eliminar empleado {employee.name}")

    #Método para gestionar reservaciones
    def manage_reservation(self, room, guest_name, action):
        if action == "check_in":
            room.check_in(guest_name)
            self.assigned_tasks.append(f"Check-in de habitación {room.get_room_number()} para {guest_name}")
        elif action == "check_out":
            room.check_out()
            self.assigned_tasks.append(f"Check-out de habitación {room.get_room_number()}")


def main():
    #TESTING
    print("=================================================================")
    print("Test Case 1: Create an Employee.")
    print("=================================================================")
    employee1 = Employee(1, "John Doe", "Receptionist", 30000)

    if employee1.get_emp_id() == 1:
        print("Test PASS. The parameter emp_id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_name() == "John Doe":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_position() == "Receptionist":
        print("Test PASS. The parameter position has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_salary() == 30000:
        print("Test PASS. The parameter salary has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    # Position and Salary Update Test
    print("=================================================================")
    print("Test Case 2: Update Employee's Position and Salary.")
    print("=================================================================")
    employee1.set_position("Manager")
    employee1.set_salary(50000)

    if employee1.get_position() == "Manager":
        print("Test PASS. The employee's position has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_position().")

    if employee1.get_salary() == 50000:
        print("Test PASS. The employee's salary has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_salary().")

if __name__ == "__main__":
    main()
