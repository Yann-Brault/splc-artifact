# splc-artifact



[![DOI](https://zenodo.org/badge/627923302.svg)](https://zenodo.org/badge/latestdoi/627923302)

Reproduction package for SPLC 2023

The project has been develop on Linux.
It has been tested on different OS: Linux (Ubuntu 22.04) and MacOS. It has also been tested on several web navigator: Firefox and Chrome.

# Run and stop the project on Docker

## Dependencies

You need a terminal with bash, Docker and Docker compose.

Before execution make sure your docker deamon is running.
If the execution crash beacause of permissions reason, run it with sudo.

## To run

To run the projet use the command `./start.sh`

If the container is up and running you should see a similar output:

```
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES

947476ba0e59 splc-artifact "uvicorn app.main:ap…" 1 second ago Up Less than a second 0.0.0.0:5050->5000/tcp, :::5050->5000/tcp splc-application

```

Application is running at this [link](http://localhost:5050/)

You can find information about reproduction scenarios further down on this document.

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
- [xmltodict](https://pypi.org/project/xmltodict/)

Then run the command `uvicorn app.main:app --port 5000 --host 0.0.0.0`

This will launch a server and make the app running [here](http://localhost:5000/)

Feel free to modify the port.

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
