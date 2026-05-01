# Percy Python Sample

This project uses `pytest`, `selenium`, and `percy-selenium` to capture a Percy visual snapshot from a Selenium-driven browser.

## Prerequisites

- Python 3.9+ (recommended)
- Node.js 16+ (required to run the Percy CLI)
- A Percy project token from BrowserStack Percy
- Google Chrome installed

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Install or update Percy CLI (project pins `@percy/cli` in `package.json`):

```bash
npm install
```

To upgrade the CLI to the latest published version anytime:

```bash
npm install @percy/cli@latest --save-dev
```

4. Set your Percy token:

```bash
export PERCY_TOKEN="your_percy_project_token"
```

## Run tests with Percy

Run the test suite through Percy so snapshots are uploaded:

```bash
npx percy exec -- pytest -v
```

## What this test does

The test in `test_sample.py`:

- Opens the URL configured in the test
- Waits until `document.readyState` is complete, then waits 5 seconds before snapshot
- Captures a Percy snapshot with the name defined in the test
- Closes the browser

## Troubleshooting

- If `percy` is not found, ensure Node.js is installed and run `npm install`, then use `npx percy exec -- …`.
- If upload fails, verify `PERCY_TOKEN` is set correctly.
- If browser startup fails, update Chrome and rerun.
