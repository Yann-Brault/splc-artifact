import json

import xmltodict
from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.generator.generator import NbGenerator

from .models import Configuration

FEATURES_MAP_PATH = './static/maps/featuresMap.json'
NOTEBOOKS_DIR_PATH = './static/Notebooks'
CONFIG_TEMPLATE_PATH = './static/configurationTemplate.json'

features_map = None
with open(FEATURES_MAP_PATH, 'r') as file:
    features_map = json.load(file)


configurator_router = APIRouter()


@configurator_router.get("/app")
async def root():
    return {"message": "you are at root"}


def write_config(config: str) -> str:
    """
    Transform the received configuration which is an xml string into a stringify json object.

    Parameters
    ----------

    config : str
        the config attribute of the Configuration data model

    Returns
    -------

    config_json : str
        a stringify json object that contains the config content
    """

    obj = xmltodict.parse(config)
    config_json = json.dumps(obj)
    return config_json


def extract_solution_configuration(content: str) -> list:
    """
    Go through the whole configuration that is equivalent to the feature Model and operate in multiple phases.
    First go through the all thing to find the range of the solution part and then extract it into the Solution list.
    Then creates a dict that contains name of all known artifacts of our artifacts library.
    Then compare selected features with known artifacts and if known put it into the configuration dict.

    Parameters
    ----------

    content : str
        the stringify json object containing the whole configuration

    Returns
    -------

    configuration : dict
        a dict containing only selected solutions of the configuration
    """

    content = json.loads(content)
    feature_list = content["configuration"]["feature"]

    sol_index = None
    src_index = None

    for index, feature in enumerate(feature_list):
        if feature["@name"] == "Solution":
            sol_index = index
            continue
        if feature["@name"] == "Sources":
            src_index = index
            break

    Solutions = feature_list[sol_index:src_index]
    configuration = []
    for sol in Solutions:
        if sol["@automatic"] == "selected" or sol["@manual"] == "selected":
            configuration.append(sol['@name'])
    return configuration


def fit_for_generator(config: list) -> dict:
    """
    Templating step to create a suitable configuration for generation

    Parameters
    ----------

        config : dict
        dict that contains all known and selected features of the client configuration

    Return
    ------

        fit_config : dict
        the same content as config but templated according to generator's need.
    """

    generator_config = None
    with open(CONFIG_TEMPLATE_PATH, 'r') as file:
        generator_config = json.load(file)
    for name in config:
        if name in features_map['features'].keys():
            artifact = features_map['features'][name]
            if artifact['dir'] == 'Algo' or artifact['dir'] == 'NN':
                generator_config['Train']['modelTraining'].append(f"{name}")
                generator_config['Valid']['prediction'].append(f"{name}")
                generator_config['Test']['prediction'].append(f"{name}")
            elif artifact['dir'] == 'Augmentation' or artifact['dir'] == 'Normalization' or artifact['dir'] == 'Transformation' or artifact['dir'] == 'FeatureEngineering':
                generator_config['Train']['dataTreatment'].append(f"{name}")
                if name != 'Smote':
                    generator_config['Valid']['dataTreatment'].append(
                        f"{name}")
                    generator_config['Test']['dataTreatment'].append(f"{name}")
            elif artifact['dir'] == 'Metrics':
                generator_config['Valid']['evaluation'].append(f'{name}')
                generator_config['Test']['evaluation'].append(f'{name}')
    return generator_config


@ configurator_router.post("/generate")
async def generate(payload: Configuration):
    """
    Receive request body from user as custom data object Configuration
    First step extract it and transform xml into json
    Second step extract selected and known features that we can generate
    Third step, fit it according to generator's template
    Then create generator with this configuration and generate the notebook
    Finally launch notebook in jupyter and return.

    Parameters
    ----------

        payload: Configuration
        Request body containing the generated configuration as stringify xml

    Return
    ------

        api response
    """

    config_json = write_config(payload.config)
    config = extract_solution_configuration(config_json)
    to_generate = fit_for_generator(config)
    generator = NbGenerator(to_generate)
    generator.generate(f'{NOTEBOOKS_DIR_PATH}/experiment_notebook.ipynb')
    # subprocess.run(['sh', './spawner.sh'])
    # url = 'http://localhost:5000/config/redirect'
    # return FileResponse(path=f'{NOTEBOOKS_DIR_PATH}/test_download.ipynb', media_type="application/octet-stream")
    return {"message": "notebook experiment_notebook generated"}


@ configurator_router.get("/download")
async def download():
    return FileResponse(path=f'{NOTEBOOKS_DIR_PATH}/experiment_notebook.ipynb', media_type="application/octet-stream")


# @ configurator_router.get("/config/redirect")
# async def redirect():
#     return RedirectResponse("http://localhost:5390/lab")
