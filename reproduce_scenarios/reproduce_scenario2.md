# Overview of Scenario 2: Reuse, complete, and generate notebook

The goal is for you to reproduce the scenario depicted in the _section 5.3_ of the paper.
With this scenario, we aim to evaluate how our approach, through its configuration and generation capabilities, helps the user to compose a solution that experiments only partially cover.

Detailed steps are given to you in order to replicate each step of the scenario.

**Disclaimer**:

We assume from here that you are running the project with Docker as explained in the [README file](../README.md).

**Checkboxes rule**:

- One click to check ![enable](../assets/all/enable.png)

- two clicks to disable ![disable](../assets/all/disable.png)

- Three clicks (total) to reset a checkbox

If a checkbox is grey (see image), it has been automatically checked or disabled by the system due to constraint propagation.

- auto check ![auto enable](../assets/all/auto_enable.png)

- auto disable ![auto disable](../assets/all/auto_disable.png)

## Data

This experience reproduces a situation where the replicator only clones a notebook and not a complete experiment, so no datasets are provided with the cloned product.

However, if the replicator, wants to clone the experiment instead of the notebook, datasets will be provided along with the notebook and the configuration. Please know that cloning a full experiment is the scenario depicted in [scenario 1](./reproduce_scenario1.md)

## Protocol

### Run the project

1. Exec start script -> `./start.sh`

2. Go to this url: [http://localhost:5050/](http://localhost:5050/) to access the main application.

You will see this web page:

![Page visual](../assets/reproduce/app_full_page.png)

### Initialize the configurator

**The web page must be reloaded between each scenario**

3. In the section _Feature Model Selection_, click on _browse_ button.

4. Go through your files, to the project directory. Once you're in, go into _static_, _illustration_test_case_, and select _illustrative_fm_scenario2.xml_.

path: `path_to_project_dir/static/illustration_test_cases/illustrative_fm_scenario2.xml`

Once it is done, you should see something like this:

![Text area with fm loaded](../assets/scenarios/scenario_2/fm_loaded_scenario2.png)

5. Now, click on the button _generate the configurator_.

You are now in the configuration process.

You should now see this on your screen :

![Valid and incomplete](../assets/reproduce/configuration_process.png)

The area at the top is present across all tabs. It keeps track of all automatically selected or deselected features due to constraint propagation.

### Unfolding the scenario: Reuse, complete, and generate notebook

#### Step 1 of scenario 2 unfolding

6. Since you already are in the tab _Initial Data_, you can check, with one click on the checkbox, the **TimeSeries** option and **PartiallyLabelled** option. Then you can disable **NormalizedData** by double clicking on the checkbox.

You should have this result:

![InitialData](../assets/scenarios/scenario_1/initialData_scenario1.png)

> If you click on tab _Past Experiments_ you can confirm that the **XP1** has been automatically disabled, but the **NB1** is still enabled. As explained in the paper, this is due to the fact that the **XP1** configuration is not compatible with the current one, but the notebook **NB1**, however, is still compatible due to the fact that the algorithm is able to deal with partially labelled data.

![past application](../assets/scenarios/scenario_1/past_appli_scenario1.png)

#### Step 2 of scenario 2 unfolding

7. You can now click on the tab _Business Requirements_ in order to complete them. Then, you can check the options **NovelAnomaliesEmergeInProd**, **PatternAnomaly**, and **Microcontroller** as it will be deployed on this type of system.

![InitialProblem](../assets/scenarios/scenario_2/initialProblem_scenario2.png)

> If you click on tab _ML Artifacts_ you can confirm that two ML artifacts have been automatically disabled, **CNN** and **Resnet**, as they are not suitable for handling new anomalies in production.

![solution](../assets/scenarios/scenario_1/solution_scenario1.png)

> If you now click on tab _Past Experiments_, you can confirm that **XP1** is still disabled and **XP2** and **XP3** are now disabled too. About notebooks, all are still available.

![past appli](../assets/scenarios/scenario_2/past_appli_scenario2.png)

#### Step 3 of scenario 2 unfolding

8. You can now go back to the tab _ML Atifacts_, go to the bottom of the page, and check _QuantizeNN_ by clicking on the checkbox once. Due to constraints linked to the selection, you should have such a configuration:

![solutionPropagated](../assets/scenarios/scenario_2/solution_propagated_scenario2.png)

> Constraint 5 in Fig. 7 (in the paper) rules out all the non-neural network models, and constraint 15 in Fig. 7 (in the paper) rules out LSTMAE as it is not compatible with quantizing neural networks. At this stage all the experiments are ruled out, additionally, the notebook **NB1** is ruled out too because it uses LSTMAE.

#### Step 4 of scenario 2 unfolding

9. At this stage, if you go back to the _Past Experiments_ tab, you can confirm that all XPs are disabled and that the **NB1** is too. You are able to reuse **NB2** or **NB3**. You can check the **NB2** to add its ML artifacts to your configuration.

![past appli 2](../assets/scenarios/scenario_2/past_appli2_scenario2.png)

> The solution that you configured is composed of the artifacts from the **NB2** and a new artifact **QuantizeNN**.

#### Step 5 of scenario 2 unfolding

10. Go back to the top of the page and click on the _Initialize_ tab.

11. Go down the page to find the _Export Configuration_ section, and then click on the _Export Current Configuration_ button. You should see text appear in the text area. It is your complete configuration as XML formatted text.

You should see this on your screen:

![export](../assets/scenarios/scenario_2/export_scenario2.png)

12. Then click on the _Generate Notebook_ button. If it worked correctly you should see a popup window saying that the notebook has been generated.

![popup window](../assets/reproduce/popup.png)

13. Finally, click on the _Download_ button, and the notebook should be downloaded. Depending on your browser settings, you might be asked where you want to save the file. Save it where it will be easy for you to find it.

### Extra steps

You might want to download the original notebook that you reused. In order to do so:

14. Go back to the top of the page and click on the _Past Experiments_ tab. Go down to the clone form. Click on the select menu in order to display options, then select the notebook option that matches the one you reused.

![selectMenu](../assets/scenarios/scenario_2/clone_reuse_scenario2.png)

Finally, you can click on the button _clone_.

This should trigger the download of the notebook as a **zip file**. Depending on your browser settings, you might be asked where you want to save the file. Save it where it will be easy for you to find it.

Once you have unzipped, you should have a directory with this structure:

NB2_electrical_engine_sound_anomaly_detection/  
&nbsp;&nbsp;&nbsp; NB2_electrical_engine_sound_anomaly_detection.ipynb  
&nbsp;&nbsp;&nbsp; current_config.xml

**As you only cloned a notebook and not a full experiment, datasets ARE NOT provided with the notebook.**

However, if you want to be able to run this notebook in particular, you can refer to the [scenario 1](./reproduce_scenario1.md)

### End

You can open notebooks in order to check their construction.

**The generated notebook, the one downloaded at step 13 IS NOT executable because adapted data import steps are not generated, and more broadly they are generated as a base product for the user to work on, not as a final product.**

### Conclusion

So with this scenario, you have been able to retrieve several past notebooks and reuse one by adding a new feature in order to generate a new notebook that well suits your problem. You were also capable to clone the reused product to compare it with the new notebook.
