# Create Poetry to new project
- `poetry new poetry_101` : create a new poetry project
- `poetry new poetry_101 --name src` : create new poetry project with config name 
- `poetry new --src rp-poetry` : src/rp-poetry 
- `poetry env list`
- `poetry env use python3.12`
- `poetry config --list`
- `poetry env list` : list all environment
- `poetry add -D pytest` : install dev package
- `poetry run pytest` : run testing 
- `poetry lock` : add package to poetry.lock
- `poetry lock --no-update` : lock poetry.lock 
- `poetry run python3` : open python in terminal
- `poetry show --help` : show all packages in env 
- `poetry update requests beautifulsoup4` : update dependencies 
- `poetry add pytest@lestest --dev` : add dev dependency
-  `poetry list` : list all command of poetry

# Add Poetry to an Existing Project
- `poetry init` : initialize to existing project
- `poetry run python3 hello.py` : run python file via poetry env 
- ``poetry add `cat requirements.txt` `` : Use an Existing requirements.txt File
- `poetry export --output requirements.txt `: create requirements.txt from peotry.lock
- `poetry export --output requirements.txt --dev` : create requirements.txt from peotry.lock + dev dependencies 


[Tutorial](https://realpython.com/dependency-management-python-poetry/)