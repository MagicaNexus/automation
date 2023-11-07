"""Main ()"""
import argparse
from dotenv import load_dotenv  # Import this at the top
from scripts import turosana  # , another_script

# Load the environment variables from the .env file
load_dotenv()

def main():
    """Run the script"""
    parser = argparse.ArgumentParser(description='Run automation scripts.')
    parser.add_argument('turosana', help='Run the turosana script')
    args = parser.parse_args()

    if args.script == 'turosana':
        turosana.run()
    elif args.script == 'another_script':
        print("Running another script")
        #another_script.run()
    else:
        raise ValueError(f"Unknown script: {args.script}")

if __name__ == "__main__":
    main()
