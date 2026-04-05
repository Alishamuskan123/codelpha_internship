# TASK 3 Alternative: Extract Email Addresses from a Text File
# This script finds all email addresses in a text file and saves them

import re

def extract_emails():
    print("=" * 40)
    print("EMAIL EXTRACTOR TOOL")
    print("=" * 40)
    
    # Get file names from user
    input_file = input("\nEnter input text file name (e.g., text.txt): ")
    output_file = input("Enter output file name (e.g., emails.txt): ")
    
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Find all email addresses using regular expression
        # Simple email pattern: something@something.something
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, content)
        
        # Remove duplicates by converting to set, then back to list
        unique_emails = list(set(emails))
        
        # Save to output file
        with open(output_file, 'w') as file:
            for email in unique_emails:
                file.write(email + '\n')
        
        # Display results
        print("\n" + "=" * 40)
        print(f"✓ Found {len(unique_emails)} unique email address(es)!")
        print(f"✓ Saved to: {output_file}")
        print("\nEmails found:")
        for email in unique_emails:
            print(f"  • {email}")
        
    except FileNotFoundError:
        print(f"✗ Error: '{input_file}' not found!")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

# Run the program
extract_emails()