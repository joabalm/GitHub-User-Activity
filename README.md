
# GitHub User Activity CLI

This is a command-line interface (CLI) tool to fetch and display the latest public activities of a specified GitHub user. The tool makes use of the GitHub API to retrieve user events and outputs the data in JSON format.

## Features

- Fetch the latest public activities for any GitHub user.
- Simple and easy-to-use command-line interface.

## Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)

## Installation

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/your-username/github-user-activity-cli.git
   cd github-user-activity-cli
   ```

2. Install the required Python package:
   ```bash
   pip install requests
   ```

## Usage

Run the script using the command line with the following syntax:

```bash
python script_name.py user.activity <github_username>
```

### Example:

To fetch the public activities of the GitHub user `joabalm`, run:

```bash
python user_activity.py user.activity joabalm
```

This will output the recent public events of the user in JSON format.

## How It Works

- The script sends a GET request to the GitHub API endpoint for user events: `https://api.github.com/users/{username}/events`.
- If the request is successful (status code 200), the script prints the JSON data containing the user's activities.

## Error Handling

- If the GitHub API request fails (e.g., due to a non-existent user or network issue), the script will not output any data.
- Ensure the GitHub username provided exists and is correct.

