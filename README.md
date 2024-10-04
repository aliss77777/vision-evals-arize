# Image Content Evaluation Tool

## Description

This tool processes and evaluates images for various content checks using the Claude AI model. It analyzes images for potential safety concerns, biases, and sensitive content based on predefined categories like violence, explicit content, cultural sensitivity, and more.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/image-content-evaluation-tool.git

2. Set up virtual environment and install dependencies:
   ```bash
   python3 -m venv [YOUR_VIRTUAL_ENV_NAME]
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variables:
- ANTHROPIC_API_KEY=<your_anthropic_api_key>
- ARIZE_SPACE_ID=<your_arize_space_id>
- ARIZE_API_KEY=<your_arize_api_key>

## Usage

1. Run the jupyter notebook making sure to set the correct python kernel for your virtual environment
   
## Features

- Claude AI model for content evaluation
- Arize for data storage and visualization
- Jupyter notebook for easy data processing and visualization

## Configuration

- Add your Anthropic API key to the .env file.
- Modify the content_checks and content_check_examples in helper_functions.py to add or change evaluation categories.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
