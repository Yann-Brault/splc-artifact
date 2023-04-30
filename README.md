# splc-artifact

software artifact for splc 2023

# Run and stop the project on Docker

## Dependencies

You need a terminal with bash, Docker and Docker compose.

Before execution make sure your docker deamon is running.
If the execution crash beacause of permissions reason, run it with sudo.

## To run

To run the projet use the command `./start.sh`

If the container is up and running you should see a similar output:

```
CONTAINER ID   IMAGE           COMMAND                  CREATED        STATUS                  PORTS                                       NAMES
947476ba0e59   splc-artifact   "uvicorn app.main:ap…"   1 second ago   Up Less than a second   0.0.0.0:5050->5000/tcp, :::5050->5000/tcp   splc-application
```

Go to this [link](http://localhost:5050/) and click the button in order to generate the notebook.

Notebook is generated in the file system of the docker container.
In order to display the content of the generated notebook (as a json file), follow these steps:

- Go into a terminal
- Execute this command `docker exec -it splc-application sh`
- you will see a prompt like this `/code # `
- you can now execute classic shell commands
- So if you use `ls` you will be able to see the container file system
- The output of this command is:
  - app/
  - static/
  - requirements.txt
  - hello_world.ipynb (if you have generated the notebook)
- To display the content as a json file, execute the command `cat hello_world.ipynb`
- You can look for the "cells" key that is a list of all cells composing the document
- execute `exit` to quit the container shell

## To stop

To stop the project use the commande `./stop.sh`

# Run and stop via full installation (Only on linux installation)

## Dependencies

you need python 3.8 at least and pip installed.

## To run

At the root of project directory, in a terminal:

Run the command `pip install --no-cache-dir --upgrade -r ./app/requirements.txt`

It will install :

- [fastapi](https://fastapi.tiangolo.com/)
- [pydantic](https://docs.pydantic.dev/)
- [uvicorn](https://www.uvicorn.org/)
- [nbformat](https://github.com/jupyter/nbformat)

Then run the command `uvicorn app.main:app --port 5000 --host 0.0.0.0`

This will launch a server and make the app accessible at adress `http://localhost:5000/`

Feel free to modify the port.

Go to the given address and click the button to generate the notebook.

The notebook is generated at the root of the projet directory.

## To stop

in your terminal execute `ctrl+c`

# Scenarios reproduction

This artifact acts as a reproduction package, hence you will find files that guides you to reproduce validation scenarios used in the paper to validate our approach.

## Scenario 1

At this [link](https://anonymous.4open.science/r/splc-artifact-files/reproduce_scenarios/reproduce_scenario1.md), or in the directory _reproduce_scenarios_ you can find the file reproducing the scenario 1 of section 5.2 in the paper. It gives a detailed list of steps to follow. The goal of this scenario is to realize a problem specification base search to find a reusable solution and clone it.

## Scenario 2

At this[link](https://anonymous.4open.science/r/splc-artifact-files/reproduce_scenarios/reproduce_scenario2.md), or in the directory _reproduce_scenarios_ you can find the file reproducing the scenario 2 of section 5.3 in the paper. It gives a detailed list of steps to follow. The goal of this scenario is to realize a problem specification base search. The search does not provides a suitable and working solution, but you are able to find a notebook that can be suitable by extending it with a new ML artifact.

## Scenario 3

At this [link](https://anonymous.4open.science/r/splc-artifact-files/reproduce_scenarios/reproduce_scenario3.md), or in the directory _reproduce_scenarios_ you can find the file reproducing the scenario 3 of section 5.4 in the paper. It gives a detailed list of steps to follow. The goal of this scenario is to realize a problem specification base search. The search does not provides any suitable solution. The objective here is to hand-pick ML artifacts composing the notebook in order to create a new product not available in the system.
