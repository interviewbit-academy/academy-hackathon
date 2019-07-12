## Welcome to InterviewBit Academy

# Day 1 covers: (Find these inside week-0/day-1)
* Bash
    * `segregate_photos.sh`: Segregate photos by years. Run this: `cd week-0/day-1/photos` and then run script like this: `bash ../segregate_photos.sh`
    * `sleepy.sh`: Play music for 15 mins and then turn off music. Run like this: `bash sleepy.sh`
    * Good resource for starting out with bash: https://linuxconfig.org/bash-scripting-tutorial-for-beginners
* Git
    * `git init`: Initialize a git repository on local.
    * `git add filename`: Add a file to track it using git.
    * `git commit`: Create new version of your project.
    * `git push origin master`: Push your updated local code on remote git server, i.e Github in our case.
    * `git clone https://github.com/interviewbit-academy/academy-hackathon`: Clone a remote repository in your local machine.
    * Good resource to learn about git: https://www.atlassian.com/git/tutorials/what-is-version-control

# Day 1 Assignment:
Download Dark Knight HD wallpapers using bash script from this URL: https://wallpapercave.com/dark-knight-hd-wallpaper

### Steps:
* Go to this URL: https://github.com/interviewbit-academy/academy-hackathon
* Fork the repository. There is a fork button in top right
* Clone the forked repo. Example: `git clone https://github.com/shivtej1505/academy-hackathon`. This will copy the codebase to your local filesystem
* Add you script under day-1 in week-0. Do `git add your_script.sh` and `git commit -m "some commit message"`
* Second last step is pushing it on remote git server i.e Github. Use this command: `git push origin master`
* Final step is too make a Pull Request here: https://github.com/shivtej1505/academy-hackathon

# Day 2 covers: (Find these inside week-0/day-2)
* Git - few more important flows
    * Git recap: Checkout archived video for the example.
    * Branching and merging in git. How to make a pull request and review?
* MVC using Flask as framework
    * What is virtual environment?
    * How data flows from server to client?
    * What is model, view & controller?

# Day 3 covers: (Find these inside week-0/day-3)
* MVC using Flask
* CRUD
* APIs

# Day 3 Class Assignment:
Implement a ToDo app in Flask.

### Steps:
1. Go to this URL: https://github.com/interviewbit-academy/academy-hackathon
2. Fork the repository. There is a fork button in top right
3. Clone the forked repo. Example: `git clone https://github.com/shivtej1505/academy-hackathon`. This will copy the codebase to your local filesystem.
4. Go to day-3 in week-0. Run this command: `source setup.sh`. This will setup virtual environment and install flask.
5. Create a new branch: `git checkout -b YOUR_BRANCH_NAME`
5. Implement the basic page. Add you files in git. Commit you code and push using this command: `git push origin YOUR_BRANCH_NAME`
6. Go to your forked repo. Make a pull request in master from the branch YOUR_BRANCH_NAME.
7. Review your pull request. Merge it if it looks good. Repeat from step 5 until your project is finished.


# Day 3 Homework:
* Again go through Flask Tutorial(http://flask.pocoo.org/docs/1.0/tutorial/) with the knowledge of MVC.
* Complete the ToDo App:
    * Connect Model with the DB.
    * Write view in separate file.
    * Add another parameter in URL `num`, which indicate how many todos a user want to view.
    * Make a pull request in original repository with screenshots.
