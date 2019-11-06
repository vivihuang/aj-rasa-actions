## aj-lithuania for Rasa actions
This is a repository showing an example bot and the setup needed to run it with Rasa.

## Steps to Setup Rasa actions with local mode

### Create virtual env with python3
use `python3 -m venv venv` or `python -m venv venv` to create venv

### Enable to use virtual env
use `source venv/bin/activate` to enable venv

### Upgrade pip if needed
`pip install --upgrade pip`

### Install dependencies
`pip install -r requirements.txt`

### Run actions
`make run-actions`

## Steps to Setup Rasa actions with Docker

### Build docker image
`docker build . -t aj-lithuania`

### Run with docker
`docker run -d --name rasa-action-server -p 5055:5055 aj-lithuania`
