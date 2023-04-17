# About

This file is a tutorial. The goal is for you to understand how to use the configurator and at the same to assert that the software works as intended.

This protocol is only about reproducing the feature selection process.
Other files are here to help you reproduce the problem configuration as a whole.

**Disclaimer** : We assume from here that you are running the project with Docker as explained in the README file.

## Protocol

### Run the projet

1. Exec start script -> `./start.sh`
2. Go on this link -> [here](http://localhost:5050/)

You will see this web page:

> image here

### Generation protocol

3. In the section _Feature Model Selection_, click on browse.
4. Go through your files, to the project directory. Once you're in, go into _Static_, _featureModel_, and select _fm.xml_.
   `_path_to_project_dir_/splc-artifact/splc-artifact-main/static/featureModel/fm.xml`

Once it is done, you should see something like this:

> image here

5. Click on generate the configurator.

You are now in the process of configuration.
You can go through the different tabs and you will see a lot of options.

The one we are interested in is _Solution_, Click on this one.

6. In order to reproduce the experiment notebook, you have to select

   - Random forest
   - Robust scaler
   - FScore

7. Once it is done, go back at the top of the page and click _initialize_

8. Go down and click on _export current configuration_. You should see text appaer in the text area. It is your complete configuration as xml text.

9. Then click on the _Generate notebook_ button. If it worked correctly you should see a popup window saying that the notebook has been generated.

10. Finally, click on the download button, and the notebook should be downloaded.

### Comparison

In order to compare the notebook you juste generated and the one that was the base model:

11. Firstly, open the one in your downloads with an ide, or jupyter notebook / lab. It should contains cells, from both type, code and markdown.

12. Go back to the projet directory and open the base model that is at the following path (once again with an ide, or jupyter notebook / lab)
    path: `_path_to_project_dir_/splc-artifact/splc-artifact-main/static/Notebooks/experiment_notebook.ipynb`

You can now compare both of them.
