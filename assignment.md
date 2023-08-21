# Git Task
Git Evaluation Task

1. Repository Setup:
    - Created a Git repository on web and cloned it on the local Machine.
    - Repo Link: https://github.com/AhmedYar45/task

2. Feature Development:
    - Created a new branch named feature/add-login
    - using command "git checkout -b feature/add-login"
    - In the branch, make a code change in the app.py file
    - Add a comment with your name and a welcome message.
    - Commit the change
    - "git add app.js"
    - "git commit -m "Add welcome message in app.js"

3. Pre-Commit Hook:

    - Set up a pre-commit hook that enforces coding standards. Create a .flake8 and the link-check.py file in the root of

my repository and configure it to run linting or formatting tools

- CODE

- [flake8]

max-line-length = 80

exclude = .git,pycache,venv


4. Pull Request:

    - Push your feature branch to your forked repository on GitHub:
    - "git push origin feature/add-login"
    - Create a pull request from your feature/add-login branch to the original repository's main branch on GitHub.

5. Post-Commit Hook:

    - Set up a post-commit hook that sends a congratulatory message to a designated whistleit channel. You'll need
      administrative access to the server hosting your Git repository for this step.

    - CODE:

		#!/bin/bash

		 Replace 'YOUR_WEBHOOK_URL' with the actual Slack webhook URL
		Whistleit_URL="YOUR_WEBHOOK_URL"

		 This is an example congratulatory message
		MESSAGE="Congratulations! A new commit has been merged."

		 Post the message to the Slack channel
		curl -X POST -H "Content-type: application/json" --data "{\"text\":\"$MESSAGE\"}" "$Whistleit_URL"
6. Webhook Notifications:
    - Now, whenever a commit is made a congratulatory message is delivered to our Whistle.it server
