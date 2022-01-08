# minimal_image_project

This package contains the minimal structure to push a typical image classification project in production

## Structure :

We propose a two-services structure:
- the backend will run in a container on google cloud run
- the frontent will run on heroku

### Backend part:
- the code to train the model is in `minimal_image_project_back/minimal_image_project_back`
  - the basic provided model is a tensorflow ConvNet, with binary classification as output
- the code for the api is in `minimal_image_project_back/api`
  - the api is managed by fastapi
  - the api is served by a uvicorn server


## Steps to reproduce the deployement :
Follow thse steps to reproduce the toy example provided, and make the necessary adaptations to your project

*Nota* : most of the commands are available in the makefiles of each part


|step|instructions   | adaptations|
|---|---|---|
|Clone this repo | `git clone https://github.com/bdepebhe/minimal_image_project.git` | |
|Install back end dependencies locally | `cd minimal_image_project_back & pip install -r requirements_docker.txt`| Dont forget to add other specific required package to `requirements_docker.txt`. Only those used in the container at prediction time.|
|Train the model   | `cd minimal_image_project_back & make train_model` | Your model will probably trained by a dedicated piece of code on another machine, such as on google colab or other. In this case, just copy the fitted model (see https://www.tensorflow.org/tutorials/keras/save_and_load)<br /> Alternatively you can use the .h5 format |
|Run the API locally | `cd minimal_image_project_back & make test_api_loccally` | Edit `api/fast.py` : change the location of the model (might be a h5 file), or the prediction output format.|
|
