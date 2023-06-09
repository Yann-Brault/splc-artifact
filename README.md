# splc23-taming-diversity-artifact

[![DOI](https://zenodo.org/badge/627923302.svg)](https://zenodo.org/badge/latestdoi/627923302)

Reproduction package for the paper entitled "Taming the Diversity of Computational Notebooks" at SPLC 2023

## Overview

The code in this package constructs and executes the tool to use our approach. To reproduce scenarios depicted in the paper, guidelines are to find in the directory _reproduce_scenarios_. In this directory, there are three different files (one for each scenario).
The replicator should expect the tool to run in less than 5 minutes if she has a working Docker setup. Each scenario can be replicated in less than 15 minutes.

## Data Availability and Provenance Statements

Three datasets are provided in this reproduction package. Two of them are synthetic data generated by ourselves, and the third dataset is publicly available.

| Data name                                     | Location                                        | Provided | Citation                                                                                                                                                                                |
| --------------------------------------------- | ----------------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DS1_motor_vibration_acquisition_error         | /static/illustration_test_cases/assets/dataset/ | TRUE     | Generated                                                                                                                                                                               |
| DS2_electrical_engine_sound_anomaly_detection | /static/illustration_test_cases/assets/dataset/ | TRUE     | Grollmisch, Sascha, Abeßer, Jakob, Liebetrau, Judith, & Lukashevich, Hanna. (2019). IDMT-ISA-Electric-Engine Dataset (1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7551261 |
| DS3_motor_vibrations_bearing_defect           | /static/illustration_test_cases/assets/dataset/ | TRUE     | Generated                                                                                                                                                                               |

## Requirements

### Software Requirements

- Bash scripts execution (Linux, Mac Os, git bash, etc.).
- For running it as a container:
  - Docker (code was run with Docker 23.0.5)
  - Docker compose
- For running it directly on a computer:
  - Python (Python 3.8 at least, the artifact was developed on Python 3.10)
  - Pip

For the configuration steps, the requirements are as follows:

– a Web browser, Firefox or Chrome (both have been tested and are
compatible).

_The artifact has been developed on Linux Ubuntu 22.04. It also has been tested on the same version of Ubuntu and on an Apple machine with an Apple Silicon chip._

## Description of programs/code

- The file `index.html` in `static/configurator` is the web page that the replicator will use as the user interface.
- The program `main.py` in `app` is the backend of the architecture and is responsible for serving static files (web page).
- The program `router.py` in `app/api` is the API and is responsible for handling generation and clone requests.
- The file `Dockerfile` in `app` and `Docker-compose.yml` at root is used by `start.sh` to build the Docker image of the application and run it in a container.

### License for Code

The code is licensed under an LGPL License. See [LICENSE](./LICENSE) for details.

## Instructions to Replicators

### How to run the application using Docker

- if you are on a Unix system:
  - You can execute the bash script `start.sh` that will use the `docker-compose.yml` file
  - To stop the container execute the bash script `stop.sh`
- otherwise:

  - Run the docker compose file with the command `docker compose up -d --build`.
  - The argument `-d` will the run container in detach mode.
  - The argument `--build` will trigger the build of the `Dockerfile`.
  - Once the execution is finished, you can run the command `docker ps` to ensure that the container is running.
  - To stop the container execute the command `docker compose down`.

- Go to this url: [http://localhost:5050/](http://localhost:5050/) to access the main application.

In both cases, if the docker execution goes well, the replicator should see a prompt similar to the following:

```
CONTAINER ID   IMAGE           COMMAND                  CREATED        STATUS                  PORTS                                       NAMES
7d83851b7ce6   splc-artifact   "uvicorn app.main:ap…"   1 second ago   Up Less than a second   0.0.0.0:5050->5000/tcp, :::5050->5000/tcp   splc-application
```

### How to run the application without Docker (full installation, Linux only)

In a terminal, in the project directory:

- Run the command `pip install --no-cache-dir --upgrade -r ./app/requirements.txt`. This will install the following Python packages:
  - [Fastapi](https://fastapi.tiangolo.com/)
  - [Pydantic](https://docs.pydantic.dev/latest/)
  - [Uvicorn](https://www.uvicorn.org/)
  - [nbformat](https://github.com/jupyter/nbformat)
  - [xmltodict](https://pypi.org/project/xmltodict/)
- Run the command `uvicorn app.main:app --port 5050 --host 0.0.0.0 --reload`.
- Go to this url: [http://localhost:5050/](http://localhost:5050/) to access the main application.

If you want to stop the process:

- Hit `ctrl+c` in the same terminal

### How to run a Jupyter Notebook

#### Requirements

In order to run a Jupyter Notebook, you will need a Jupyter environment, either Jupyter Notebook or JupyterLab.

#### Instructions to install Jupyter notebook

- in a terminal, run the command `pip install notebook`, more details [here](https://jupyter.org/install)

#### Instructions to install JupyterLab

- in a terminal, run the command `pip install jupyterlab`, more details [here](https://jupyter.org/install)

In order to run a notebook:

- in a terminal go to the notebook directory
- To run with Jupyter Notebook, execute bash command `jupyter notebook`
- To run with JupyterLab, execute the bash command `jupyter-lab`.

In both cases, the command will open the JUpyter environment at `localhost:8888`

In order to run the code inside cloned notebooks, you will need Python libraries:

| Library    | command                     | Link                                                 |
| ---------- | --------------------------- | ---------------------------------------------------- |
| Tensorflow | pip install tensorflow      | [link](https://pypi.org/project/tensorflow/)         |
| Keras      | pip install keras           | [link](https://pypi.org/project/keras/)              |
| sklearn    | pip install -U scikit-learn | [link](https://scikit-learn.org/stable/install.html) |
| librosa    | pip install librosa         | [link](https://librosa.org/doc/latest/install.html)  |
| numpy      | pip install numpy           | [link](https://pypi.org/project/numpy/)              |

**All these libraries are needed to run the cloned experiment in [scenario 1](./reproduce_scenarios/reproduce_scenario1.md).**

### How to reproduce scenarios

#### Scenario 1

At this [link](./reproduce_scenarios/reproduce_scenario1.md), or in the directory _reproduce_scenarios_ you can find the guidelines to reproduce scenario 1 of section 5.2 in the paper. The goal of this scenario is to realize a problem specification base search to find a reusable solution and clone it.

#### Scenario 2

At this [link](./reproduce_scenarios/reproduce_scenario2.md), or in the directory _reproduce_scenarios_ you can find the guidelines to reproduce scenario 2 of section 5.3 in the paper. The goal of this scenario is to realize a problem specification base search. The search does not provide a suitable and working solution, but you are able to find a notebook that can be suitable by extending it with a new ML artifact.

#### Scenario 3

At this [link](./reproduce_scenarios/reproduce_scenario3.md), or in the directory _reproduce_scenarios_ you can find the guidelines to reproduce scenario 3 of section 5.4 in the paper. The goal of this scenario is to realize a problem specification base search. The search does not provide any suitable solution. The objective here is to hand-pick ML artifacts composing the notebook in order to create a new product not available in the system.
