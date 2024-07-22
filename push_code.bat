@echo off
REM Change directory to your git repository
cd /d "C:\path\to\your\repository"

REM Add all changes to the staging area
git add .

REM Prompt for a commit message
set /p commitMessage=Enter commit message: 

REM Commit the changes
git commit -m "%commitMessage%"

REM Push the changes to the remote repository
git push

REM Pause to see the result
pause
