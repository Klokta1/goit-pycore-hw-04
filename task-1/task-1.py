def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total = 0
            num_developers = len(lines)
            for line in lines:
                _, salary = line.strip().split(',')
                total += int(salary)
            average = total / num_developers
            return total, average
    except FileNotFoundError:
        print("File not found.")
        return None, None
    except Exception as e:
        print(f"Error during reading from file: {e}")
        return None, None


total, average = total_salary("salary-file.txt")
if total and average:
    print(f"Sum of salaries: {total}, Average salary: {average}")
