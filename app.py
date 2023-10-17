import subprocess

def get_current_git_branch():
    try:
        # Run the 'git branch --show-current' command to get the current branch name
        result = subprocess.run(['git', 'branch', '--show-current'], stdout=subprocess.PIPE, text=True, check=True)
        current_branch = result.stdout.strip()
        return current_branch
    except subprocess.CalledProcessError:
        # This will be executed if the 'git branch --show-current' command 
        return None

# Example usage:
current_branch = get_current_git_branch()
if current_branch:
    print(f"Current branch is: {current_branch}")
else:
    print("Unable to determine the current branch.")
