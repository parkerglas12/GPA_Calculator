import numpy as np

def get_user_input(grades_to_gpa: dict[str, float]) -> tuple[list[str], np.ndarray]:
    while True:
        try:
            num_courses: int = int(input("How many courses do you wish to input: "))
            if num_courses < 1 or num_courses > 24:
                raise ValueError("Enter an integer between 1 and 24 for the number of courses.")
            grades: list[str] = []
            credits: np.ndarray = np.zeros(shape=num_courses)
            for i in range(0, num_courses):
                grade: str = str(input(f"Please enter your grade for course #{i + 1} e.g. (A, C+, B-): ")).upper()
                credit_amount: int = int(input("Please enter the number of course credits: "))
                if grade not in grades_to_gpa:
                    raise ValueError("Please enter a valid grade.")
                if credit_amount > 8 or credit_amount < 1:
                    raise ValueError("Enter an integer between 1 and 8 for number of course credits.")
                credits[i] = credit_amount
                grades.append(grade)
        except ValueError as e:
            print(f"Error: {e}")
        else:
            return grades, credits

def main() -> None:
    grades_to_gpa: dict[str, float] = {
        "A+": 4.3, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0,
        "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, 
        "D": 1.0, "D-": 0.7, "F": 0
    }
    grades, credits = get_user_input(grades_to_gpa) 
    gpa_array: np.ndarray = np.array([grades_to_gpa[grade] for grade in grades])
    gpa: float = np.dot(gpa_array, credits) / sum(credits)
    print(f"Your GPA is: {gpa:.3f}")
    
if __name__ == "__main__":
    main()