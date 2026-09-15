import re

# Pattern for finding an email address
EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'
# Function to find all email addresses from text
def find_emails(text):
    return re.findall(EMAIL_PATTERN, text)

# Function to check whether an email is valid
def is_valid_email(email):
    return re.fullmatch(EMAIL_PATTERN, email) is not None

# Main program
if __name__ == "__main__":

    text = """
    Contact details:
    - College office: office@college.edu
    - Admission: admission.team@college.co.in
    - Student email: student123@gmail.com
    - Some invalid text: abc@, @gmail.com, hello
    - Event registration: events+2026@college.org
    """
    print("Given text:")
    print(text)
    emails = find_emails(text)
    print("Email addresses found:", len(emails))
    for email in emails:
        print("-", email)
    print("\nChecking different email addresses:")
    email_list = [
        "student@gmail.com",
        "wrong-email",
        "abc@website",
        "test@website.com",
        "hello@",
        "first.last+test@college.co.in"
    ]
    for email in email_list:
        if is_valid_email(email):
            print(email, "-> VALID")
        else:
            print(email, "-> INVALID")
