# Percy Python Sample

This project uses `pytest`, `selenium`, and `percy-selenium` to take a visual snapshot of a page that allows automation.

**Why Tesla shows “Access Denied”:** `tesla.com` sits behind Akamai bot/WAF protection. Automated browsers (including Percy + Selenium) are often blocked before real HTML loads. That is enforced on Tesla’s side; changing timeouts or Percy settings will not fix it. Use your own staging build, `localhost`, or another URL your team is allowed to hit.

By default the test opens `https://example.com`. Point at any allowed URL:

```bash
export PERCY_TEST_URL="https://your-staging.example.com"
npx percy exec -- pytest -v
```

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

- Opens `PERCY_TEST_URL` if set, otherwise `https://example.com`
- Uses a 10-second page-load timeout
- Waits until `document.readyState` is complete, then waits 5 seconds before snapshot
- Captures a Percy snapshot named `Sample homepage`
- Closes the browser

## Troubleshooting

- If `percy` is not found, ensure Node.js is installed and run `npm install`, then use `npx percy exec -- …`.
- If upload fails, verify `PERCY_TOKEN` is set correctly.
- If you see **Access Denied** (often with `errors.edgesuite.net`), the CDN/WAF is blocking automation — common on sites like Tesla. Use `PERCY_TEST_URL` to snapshot staging or a permissive page instead of trying to bypass protection.
- If browser startup fails, update Chrome and rerun.
