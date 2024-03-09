![PyFetchGit Logo](./img/PyFetchGit%20(1).png)



PyFetchGit is a lightweight Python tool for fetching and installing files from GitHub repositories.

## Features

- Fetch and install files from GitHub repositories with ease.
- Automatically downloads the latest stable version from the repository.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sqvdd/PyFetchGit.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd PyFetchGit
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Replace the following variables in the script with your GitHub username, repository name, and filename to download:

    ```python
    user = ""       # GitHub Username
    repo = ""       # Repository Name
    filename = ""   # Zipfile to download
    ```
    ![PyFetchGit Logo](./img/Variable.png)

2. Run the script to download and install the specified file from the GitHub repository.

    ```bash
    python pyfetchgit.py
    ```

## Support

For any questions or issues, please open an [issue](https://github.com/sqvdd/PyFetchGit/issues).


