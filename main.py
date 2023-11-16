"""Main ()"""
import argparse
from dotenv import load_dotenv
from scripts import turosana  # Import the required script

# Load the environment variables from the .env file
load_dotenv()

def main():
    """Run the script"""
    parser = argparse.ArgumentParser(description='Run automation scripts.')
    # Change 'turosana' to a positional argument to '--script'
    parser.add_argument('--script', help='Specify the script to run', choices=['turosana', 'another_script'])
    args = parser.parse_args()

    # Compare the 'script' argument
    if args.script == 'turosana':
        turosana.run()
    elif args.script == 'another_script':
        print("Running another script")
        # another_script.run()
    else:
        raise ValueError(f"Unknown script: {args.script}")

if __name__ == "__main__":
    main()
