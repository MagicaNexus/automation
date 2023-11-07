# Automation Application

## Introduction

This application facilitates the creation of tasks in Asana based on specific emails received in Gmail. It is designed to streamline workflows by automating task creation.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- An Asana account with an access token
- A Gmail account with app-specific password enabled

## Installation

To install the Automation Application, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/MagicaNexus/automation.git
```

2. Navigate to the cloned directory:

```bash
cd automation
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Configure the application settings by:

1. Creating a `.env` file in the root directory with your Asana and Gmail credentials:

```plaintext
ASANA_ACCESS_TOKEN=your_asana_access_token
ASANA_PROJECT_ID=your_asana_project_id
ASANA_USER_ID=your_asana_user_id
ASANA_SECTION_ID=your_asana_section_id
GMAIL_EMAIL=your_gmail_email
GMAIL_APP_PASSWORD=your_gmail_app_password
```

2. Adjusting the settings in `.vscode/settings.json` if you're using VSCode as your IDE.

## Usage

To use the Automation Application, run:

```bash
python main.py turosana
```

This will execute the `turosana` script, which checks for specific emails in Gmail and creates corresponding tasks in Asana.

## Contributing

For those who wish to contribute to the application, please follow the standard fork and pull request workflow.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

If you have any questions or feedback, please open an issue in the GitHub repository issue tracker.

```

Please replace the placeholders with your actual Asana and Gmail credentials. The application uses environment variables to manage sensitive information such as API keys and user credentials.

For more detailed instructions or if you have specific questions about the application, feel free to ask.
```
