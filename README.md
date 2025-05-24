# Google ADK Hackathon

This repository contains the project developed during the Google ADK (AI Developer Kit) Hackathon. The project leverages Google's AI tools to create an innovative application.

## Project Overview

The Google ADK Hackathon is an event where developers explore and build applications using Google's AI Developer Kit. This toolkit provides access to Google's AI models and capabilities, enabling the creation of AI-powered applications.

## Getting Started

Follow these steps to set up and run the project:

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- Google ADK installed

### Installation

1. Clone the repository:

```bash
git clone https://github.com/GraysonWills/Google-ADK-Hackathon.git
```

2. Navigate to the project directory:
```bash
cd Google-ADK-Hackathon
```
3. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```
4. Activate the virtual environment:
```bash
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate  # On Windows

```
5. Install the project dependencies:
```bash
pip install -r requirements.txt
```

6. Create .env file and add your Google Gemini key from Google AI Studio:
```bash
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```
# This is one way of running it -- But we want to over the full UI so ignore this
## Running the project
Once you have set up the project, you can run the project using the ADK CLI: 

``` bash
adk web
```
This command will start the web application, and you should be able to access it through your browser at the URL displayed in the terminal (typically http://localhost:8080).

## Install custom UI
## Prerequisite:

- **Install [Angular CLI](https://angular.dev/tools/cli)**

- **Install [NodeJs](https://nodejs.org/en)**

- **Install [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)**

- **Install [google-adk (Python)](https://github.com/google/adk-python)** 
### Now:
- cd into `agent-custom-ui/adk-web` 
```bash 
sudo npm install
```
- from the adk-web dir, run
```bash
npm run serve --backend=http://localhost:8000
```
and from the main dir (aka Google-ADK-Hackathon), run 
```bash
adk api_server --allow_origins=http://localhost:4200 
```


More information in the readme in `agent-custom-ui/adk-web`
