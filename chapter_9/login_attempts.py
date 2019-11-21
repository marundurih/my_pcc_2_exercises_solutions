# This program starts from users.py
class User():
    """Class models a user profile."""
    
    def __init__(
                self,
                first_name, last_name,
                department, faculty,
                login_attempts
                ):
        """Add an attributes (login_attempts)."""
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.faculty = faculty
        self.login_attempts = login_attempts
        
    def describe_user(self):
        """
        Prints a summary of the user.
        du = describe user
        """
        full_name = f"{self.first_name.title()}{self.last_name.title()}"
        
        du = f"{full_name} is a student of {self.department}, {self.faculty}.\n"
        print(du)
        
    def greet_user(self):
        """Prints a personalized greeting to the user."""
        full_name = f"{self.first_name.title()}{self.last_name.title()}"
        print(f"Hi, {full_name}!")
        
    def increment_login_attempts(self):
        """
        Write a method that increments the value of, login_attempts by 1.
        """
        self.login_attempts += 1
        return self.login_attempts
        
    def reset_login_attempts(self):
        """
        Write another method that resets the value of, login_attempts to 0. ()
        """
        self.login_attempts = 0
        return self.login_attempts
        
# Make an instance from this class.
hm = User('h', 'm', 'economics', 'economy', 1)

# Call increment_login_attempts() several times.
while hm.login_attempts < 22:
    hm.increment_login_attempts()

# Print login_attempts to make sure it was incremented properly.
print(f"Total login attempts: {hm.login_attempts}")

# And then call reset_login_attempts()
hm.reset_login_attempts()

# Last, print login_attempts again to make sure it was reset to 0.
print(f"Reset login attempts: {hm.login_attempts}")
