# Rembg App

Web app to remove images background using [rembg](https://github.com/danielgatis/rembg) ([Demo](https://rembg.000314.xyz)).

[![Docker Build](https://github.com/Alyetama/Rembg-Online/actions/workflows/docker-build.yml/badge.svg)](https://github.com/Alyetama/Rembg-Online/actions/workflows/docker-build.yml) [![pages-build-deployment](https://github.com/Alyetama/Remove-Background-Online/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/Alyetama/Remove-Background-Online/actions/workflows/pages/pages-build-deployment) [![Vercel deploy](https://github.com/Alyetama/Remove-Background-Online/actions/workflows/vercel-deploy.yml/badge.svg)](https://github.com/Alyetama/Remove-Background-Online/actions/workflows/vercel-deploy.yml) [![Docker Hub](https://badgen.net/badge/icon/Docker%20Hub?icon=docker&label)](https://hub.docker.com/r/alyetama/rembg-app) [![Supported Python versions](https://img.shields.io/badge/Python-%3E=3.9-blue.svg)](https://www.python.org/downloads/) [![Streamlit](https://img.shields.io/badge/Streamlit-1.10.0-red)](https://github.com/streamlit/streamlit/releases/tag/1.10.0) [![PEP8](https://img.shields.io/badge/Code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)


## Deployment

```sh
git clone https://github.com/Alyetama/Rembg-App.git
cd Rembg-App
```

### Option 1: Run locally

```sh
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### Option 2: Free cloud hosting on Streamlit Cloud

- [Fork this repository](https://github.com/Alyetama/Rembg-App/fork).
- Go to [this page]( https://share.streamlit.io/deploy), select your fork under `Repository`, then click `Deploy!`.

![streamlit_cloud](https://i.imgur.com/STSB68n.png)

### Option 3: Docker

```
docker run \
    -p 8501:8501 \
    -v "${PWD}/.streamlit:/home/app/.streamlit" \
    alyetama/rembg-app:latest
```

#### Docker Compose

```
docker-compose up -d
```

##### Updating
```sh
docker pull alyetama/rembg-app:latest
```

If you're using the pre-built docker image in docker-compose, you can update the image by running:
```sh
docker-compose down
docker-compose pull
docker-compose up -d
```

## Configuration

- To configure the streamlit application, edit `.streamlit/config.toml` ([configuration reference](https://docs.streamlit.io/library/advanced-features/configuration)).
- To configure the maximum number of uploaded files (*default: 10*), set the environment variable `MAX_FILES`:
    - Option 1: Export the variable.
    ```sh
    export MAX_FILES=20
    ```
    - Option 2: Edit the value of `MAX_FILES` in `.env`.
    ```sh
    mv .env.example .env
    nano .env  # or any other text editor
    ```
    - On Streamlit Cloud: Go to the app settings -> Secrets -> `MAX_FILES = 20` -> save.


## Notes

- The very first processed image after starting the app may take few minutes, because the backend model is being downloaded for the first time.
