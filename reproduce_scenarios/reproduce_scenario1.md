# About

This file is a tutorial. The goal is for you to reproduce the scenario depicted in the _section 5.1_ of the article.

Detailed steps are given to you in order to replicate each step of the scenario.

**Disclaimer** : We assume from here that you are running the project with Docker as explained in the [README file](https://anonymous.4open.science/r/splc-artifact-files/README.md).

Checkboxes rule :

- One click to select / enable ![enable](../assets/all/enable.png)
- two clicks to deselect / disable ![disable](../assets/all/disable.png)
- Three clicks (total) to reset a checkbox

If a checkbox is grey (see image), it has been automatically enabled or disabled by the system due to constraint propagation.

- auto enable ![auto enable](../assets/all/auto_enable.png)
- auto disable ![auto disable](../assets/all/auto_disable.png)

## Protocol

### Run the projet

1. Exec start script -> `./start.sh`

2. Go on this link -> [here](http://localhost:5050/)

You will see this web page:

![Page visual](../assets/reproduce/app_full_page.png)

### Initialize the configurator

3. In the section _Feature Model Selection_, click on _browse_ button.

4. Go through your files, to the project directory. Once you're in, go into _Static_, _illustration_test_case_, and select _illustrative_feature_model.xml_.

path: `_path_to_project_dir_/splc-artifact-main/static/illustration_test_case/illustrative_feature_model.xml`

Once it is done, you should see something like this:

![Text area with fm loaded](../assets/reproduce/fm_loaded.png)

5. Now, click on the button _generate the configurator_.

You are now in the process of configuration.

You should now see this on your screen :

![Valid and incomplete](../assets/reproduce/valid_incomplete.png)

**Do not worry** about the message saying "this configuration is valid and complete".
The configuration is indeed valid, this means the loading and creation of the whole constraint system is successful.
This area is present across all tabs because it keeps track of all automatically selected or deselected features due to constraint propagation.

### Unfolding the scenario : Cloning

6. As you are in the tab _Initial Data_, you can select, with one click on the checkbox, the **time series** option and **partially labeled** option. Then you can disable **normalized data** by double clicking on the checkbox.

You should have this result:

![InitialData](../assets/scenarios/scenario_1/initialData_scenario1.png)

7. If you click on tab _Appli & Dataset_ you can confirm that the **XP1** has been automatically disabled, but the **NB1** is still enable.

(image here, coming after FM update)

8. You can now click on tab _Initial Problem_ in order to complete business requirements. Then, you can enable the option **NovelAnomaliesEmergeInProd** and **patternAnomaly**.

![InitialProblem](../assets/scenarios/scenario_1/initialProblem_scenario1.png)

9. If you click on tab _Solutions_ you can confirm that two ML components have been automatically disabled, **CNN** and **Resnet**, as specified in the article.

![solution](../assets/scenarios/scenario_1/solution_scenario1.png)

10. If you now click on tab _Appli & Dataset_, you can confirm that **XP1** is still disabled and **XP2** is enabled.

(image here, coming after FM update)

About notebooks, both **NB1** and **NB2** are available.

(image here, coming after FM update)

So, you click on the checkbox of the **XP2** firstly. Then you go to the form at the bottom of the page.

(image here, coming after FM update)

Click on the select menu in order to display options, then select the **XP2** option.

![selectMenu](../assets/scenarios/scenario_1/select_menu.png)

Finally you can click on the button _clone_.
This should trigger the download of the **XP2** project as a **zip file**. Depending on your browser settings, you might be asked where you want to save the file. Save it where it will be easy for you to find it.

Once you have unzip the project, you should have a directory with this file strucutre :

You should have a directory called _XP2_electrical_engine_sound_anomaly_detection_ and a file _current_config.xml_. This xml file is the configuration that you just realized through this tutorial.
In the directory, you will find the notebook file, _notebook.ipynb_ and the configuration file of this project, _XP2_config.xml_.
