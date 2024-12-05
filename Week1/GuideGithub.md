# Guide for Using GitHub with VisionCraft

## Steps to Fork and Clone the Repository

### Using the Browser and Git Bash

1. **Fork the Repository**  
   - Navigate to the repository in your browser.  
   - Click on the **Fork** button (usually found at the top-right corner) to create a copy in your GitHub account.

2. **Clone the Repository to Your Local Machine**  
   - Open the folder where you want to store the project on your local machine.  
   - Right-click in the folder and select **Git Bash Here** to open the terminal.  
   - Use the following command to clone the repository:
     ```bash
     git clone [repository_url]
     ```
     > Replace `[repository_url]` with the URL you copied from the green **Code** button in the repository.

---

### Using GitHub Desktop

1. **Fork the Repository**  
   - Follow the same steps as above to fork the repository in your browser.

2. **Clone the Repository**  
   - Open GitHub Desktop.  
   - Go to **File > Clone Repository**.  
   - Select the forked repository from your GitHub account or paste the repository URL.  
   - Choose a local path to save the repository and click **Clone**.

---

## Adding Your Files and Submitting Changes

### Using Git Bash

1. **Add Your Files**  
   - Follow the submission guidelines to add your files to the appropriate folders.

2. **Stage Your Changes**  
   - Open Git Bash in your project folder and type:
     ```bash
     git add .
     ```
     This stages all the changes you’ve made.

3. **Commit Your Changes**  
   - Commit the changes with a meaningful message:
     ```bash
     git commit -m "Your descriptive commit message"
     ```

4. **Push the Changes**  
   - Push your changes to your forked repository:
     ```bash
     git push
     ```

---

### Using GitHub Desktop

1. **Add Your Files**  
   - Copy or edit files directly in the folder where the repository is saved on your local machine.

2. **Stage and Commit Your Changes**  
   - Open GitHub Desktop.  
   - The application will automatically detect changes in the repository.  
   - Add a descriptive commit message in the **Summary** box and click **Commit to Main** (or the active branch).

3. **Push the Changes**  
   - Click on **Push Origin** to push your changes to your GitHub repository.

---

## Generating a Pull Request

1. Open the repository in your browser.
2. Click on the **Pull Requests** tab.
3. Select **New Pull Request**.
4. Provide a clear description of the changes and submit the pull request.

---

## Troubleshooting

- If you face errors, try searching for solutions on Google.
- If issues persist, feel free to:
  - **Direct Message (DM)** me for help.
  - Post your question in the **Discussions Group**.

---

**Note**: These steps were covered in the previous class. Ensure you understand them and reach out for help if needed.
