# Remove Background Online

Web app to remove images background ([Demo](https://rembg.vercel.app))

[![Docker build](https://github.com/Alyetama/Remove-Background-Online/actions/workflows/docker-build.yml/badge.svg)](https://github.com/Alyetama/Remove-Background-Online/actions/workflows/docker-build.yml) [![Supported Python versions](https://img.shields.io/badge/Python-%3E=3.9-blue.svg)](https://www.python.org/downloads/) [![Streamlit](https://img.shields.io/badge/Streamlit-1.9.0-red)](https://github.com/streamlit/streamlit/releases/tag/1.9.0) [![PEP8](https://img.shields.io/badge/Code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/) 


## Deployment

```sh
git clone https://github.com/Alyetama/Remove-Background-Online.git
cd Remove-Background-Online
```

### Option 1: Run locally

```sh
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### Option 2: Free cloud hosting on Streamlit Cloud

- [Fork this repository](https://github.com/Alyetama/Remove-Background-Online/fork)
- Go to [this page]( https://share.streamlit.io/deploy), select your fork under `Repository`, then click `Deploy!`.

![streamlit_cloud](https://i.imgur.com/STSB68n.png)

### Option 3: Docker Compose

```
docker-compose up -d
```

## Configuration

- To configure the streamlit application, edit `.streamlit/config.toml` ([configuration reference](https://docs.streamlit.io/library/advanced-features/configuration)).
- To configure the maximum number of uploaded files (*default: 10*):
    - Pass the maximum number after the command (e.g., `streamlit run streamlit_app.py 20`), or
    - Rename `.env.example` to `.env` and edit the value of `MAX_FILES`.
