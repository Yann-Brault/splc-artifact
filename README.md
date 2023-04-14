# splc-artifact

software artifact for splc 2023

# Run and stop the project on Docker

## Dependencies

You need a terminal with bash, Docker and Docker compose.

Before execution make sure your docker deamon is running.
If the execution crash beacause of permissions reason, run it with sudo.

## To run

To run the projet use the command `./run.sh`

If the container is up and running you should see a similar output:

```
CONTAINER ID   IMAGE      COMMAND                  CREATED                  STATUS                  PORTS                                       NAMES
bf5899bde536   rocknrwl   "uvicorn app.main:ap…"   Less than a second ago   Up Less than a second   0.0.0.0:5050->5000/tcp, :::5050->5000/tcp   rocknrwl-application
```

Go to `http://localhost:5050/` and click the button in order to generate the notebook.

Notebook is generated in the file system of the docker container

## To stop

To stop the project use the commande `./stop.sh`

# Run and stop the project on your computer

## Dependencies

you need python 3.8 at least and pip installed.

## To run

At the root of project directory, in a terminal:

Run the command `pip install --no-cache-dir --upgrade -r ./app/requirements.txt`

It will install :

- fastapi
- pydantic
- uvicorn
- nbformat

Then run the command `uvicorn app.main:app --port 5000 --host 0.0.0.0`

This will launch a server and make the app accessible at adress `http://localhost:5000/`

Feel free to modify the port.

Go to the given address and click the button to generate the notebook.

The notebook is generated at the root of the projet directory.

## To stop

in your terminal execute `ctrl+c`
