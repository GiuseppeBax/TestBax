import os

# Incorrect usage of <>
if 5 <> 10:
    print("5 is not equal to 10")

# Incorrect usage of =+ instead of +=
a = 5
b = 10
a += b
print("Value of a:", a)

# Example code with issues for static code analysis

def divide_numbers(a, b):
    result = a / b  # Potential division by zero
    return result

def unused_variable_example():
    x = 10  # Unused variable

if __name__ == "__main__":

def insecure_file_operations(file_path):
    # Security issue: Insecure use of file paths
    file_content = open(file_path, 'r').read()
    print(f"File content: {file_content}")

def sql_injection(username):
    # Security issue: Potential SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    # Execute the query (in a real application, this should be done with proper parameterization)
    print(f"Executing SQL query: {query}")

def insecure_eval(user_input):
    # Security issue: Use of eval with user input
    result = eval(user_input)
    print(f"Result of eval: {result}")

if __name__ == "__main__":
    # Example usage
    insecure_file_operations("/etc/passwd")
    sql_injection("admin' OR '1'='1' --")
    insecure_eval("__import__('os').system('ls')")