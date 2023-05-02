# splc23-taming-diversity-artifact

## Overview

The code in this package constructs and execute the tool to use our approach. To reproduce scenarios depicted in the paper, guidelines are to find for the replicator in the directory _reproduce_scenarios_. In this directory, there are three different files (one for each scenario).
The replicator should expect the tool to run in less than 5 minutes, if she has a working Docker setup. Each scenario can be replicated in less than 15 minutes.

## Data Availability and Provenance Statements

Due to very limited storage space available on the anonymous repository, dataset necessary to execute notebooks **are not** included in this reproduction package. They will be given in a public release of a Zenodo package for the artifact evaluation.

## Computational requirements

### Software Requirements

- Run within a container:
  - Docker (code was run with Docker 23.0.5)
  - Docker compose
- Run directly on computer:
  - Python (Python 3.8 at least, artifact was developed on Python 3.10)
- Web navigator:
  - Firefox or Chrome (both have been tested and are compatible)

Be aware that artifact execution is based on bash scripts execution.

_The artifact has been developed on Linux Ubuntu 22.04. It also has been tested on the same version of Ubuntu and on an Apple machine with Apple Silicon chip._

## Description of programs/code

- The file `index.html` in `static/configurator` is the web page that the replicator will use as user interface.
- The program `main.py` in `app` is the backend of the architecture and is responsible for serving static files (web page).
- The program `router.py` in `app/api` is the api and is responsible for handling generation and clone request.
- The file `Dockerfile` in `app` and `Docker-compose.yml` at root are used by `start.sh` to build the Docker image of the application and run it in a container.

### License for Code

The code is licensed under a LGPL License. See [LICENSE](https://anonymous.4open.science/r/splc-artifact-files/LICENSE) for details.

## Instructions to Replicators

### How to run application using Docker

- if you are on a unix system:
  - You can execute the bash script `start.sh` that will use the `docker-compose.yml` file
  - To stop the container execute the bash script `stop.sh`
- else:
  - Run the docker compose file with the command `docker compose up -d --build`.
  - The argument `-d` will the run container in detach mode.
  - The argument `--build` will trigger the build of the `Dockerfile`.
  - Once the execution is finished, you can run the command `docker ps` to ensure that the container is running.
  - To stop the container execute the command `docker compose down`.

In both cases, if the docker execution goes well, the replicator should see a prompt similar as the following:

```
CONTAINER ID   IMAGE           COMMAND                  CREATED        STATUS                  PORTS                                       NAMES
7d83851b7ce6   splc-artifact   "uvicorn app.main:ap…"   1 second ago   Up Less than a second   0.0.0.0:5050->5000/tcp, :::5050->5000/tcp   splc-application
```

### How to run application without Docker (full installation, Linux only)

In a terminal, in the project directory:

- Run the command `pip install --no-cache-dir --upgrade -r ./app/requirements.txt`. This will install the following Python packages:
  - [Fastapi](https://fastapi.tiangolo.com/)
  - [Pydantic](https://docs.pydantic.dev/latest/)
  - [Uvicorn](https://www.uvicorn.org/)
  - [nbformat](https://github.com/jupyter/nbformat)
  - [xmltodict](https://pypi.org/project/xmltodict/)
- Run the command `uvicorn app.main:app --port 5050 --host 0.0.0.0 --reload`.
- Go to this [link](http://localhost:5050/)
- Hit `ctrl+c` to stop the process

### How to reproduce scenarios

#### Scenario 1

At this [link](https://anonymous.4open.science/r/splc-artifact-files/reproduce_scenarios/reproduce_scenario1.md), or in the directory _reproduce_scenarios_ you can find the file reproducing the scenario 1 of section 5.2 in the paper. It gives a detailed list of steps to follow. The goal of this scenario is to realize a problem specification base search to find a reusable solution and clone it.

#### Scenario 2

At this [link](https://anonymous.4open.science/r/splc-artifact-files/reproduce_scenarios/reproduce_scenario2.md), or in the directory _reproduce_scenarios_ you can find the file reproducing the scenario 2 of section 5.3 in the paper. It gives a detailed list of steps to follow. The goal of this scenario is to realize a problem specification base search. The search does not provides a suitable and working solution, but you are able to find a notebook that can be suitable by extending it with a new ML artifact.

#### Scenario 3

At this [link](https://anonymous.4open.science/r/splc-artifact-files/reproduce_scenarios/reproduce_scenario3.md), or in the directory _reproduce_scenarios_ you can find the file reproducing the scenario 3 of section 5.4 in the paper. It gives a detailed list of steps to follow. The goal of this scenario is to realize a problem specification base search. The search does not provides any suitable solution. The objective here is to hand-pick ML artifacts composing the notebook in order to create a new product not available in the system.
