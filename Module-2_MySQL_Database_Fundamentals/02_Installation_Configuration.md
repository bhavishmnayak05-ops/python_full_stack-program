# 02. MySQL Installation & Configuration

Installing MySQL correctly is the first step toward building database-driven applications. We will look at installation on various platforms.

## 1. Installation on Windows
The easiest way is to use the **MySQL Installer**.

1.  **Download:** Go to [MySQL Community Downloads](https://dev.mysql.com/downloads/installer/) and download the "MySQL Installer for Windows".
2.  **Run Installer:** Choose the **"Developer Default"** setup type.
3.  **Check Requirements:** The installer will check for prerequisites. Follow the prompts.
4.  **Configuration:** 
    - Set the **Root Password** (Remember this! You will need it later).
    - Choose "Standalone MySQL Server / Classic MySQL Replication".
    - Finish the installation.

## 2. Installation on Linux (Ubuntu/Debian)
Open your terminal and run the following commands:

```bash
# Update your package index
sudo apt update

# Install MySQL Server
sudo apt install mysql-server

# Verify installation
mysql --version

# Run the security script to set a root password and remove insecure defaults
sudo mysql_secure_installation
```

## 3. Installation on macOS
Using **Homebrew** is the recommended method:

```bash
# Install Homebrew if you haven't
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install mysql
brew install mysql

# Start the mysql service
brew services start mysql

# Secure the installation
mysql_secure_installation
```

## 4. Basic Configuration
Once installed, you should be able to log in to the MySQL Command Line Client:

```bash
mysql -u root -p
```
Enter the password you set during installation.

### Key Tools:
-   **MySQL Command Line Client (CLI):** Lightweight, text-based interface.
-   **MySQL Workbench:** A graphical user interface (GUI) for database design, SQL development, and server administration.

## 5. Environment Variables (Windows)
To run `mysql` from any command prompt, add the MySQL bin folder to your System Path:
1. Search for "Environment Variables".
2. Edit "Path" in System Variables.
3. Add: `C:\Program Files\MySQL\MySQL Server 8.0\bin` (or your installation path).

## Summary
You should now have a running MySQL server. Whether you use the CLI or Workbench, ensure you can access the system with your root credentials.
