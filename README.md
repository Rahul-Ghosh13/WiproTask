# Python API Automation Framework

Reusable REST API automation for the Automation Exercise User Management API, built with `requests`, `behave`, and Allure.

## Project layout

```text
config/                 Environment-backed settings
src/api/client.py       Reusable requests session and user API methods
src/api/payloads.py     Request payload factories
features/               Behave feature and step definitions
tests/                  Fast mocked unit tests for the client
requirements.txt        Python dependencies
```

## Setup

From PowerShell:

```powershell
python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

The default base URL is `https://automationexercise.com`. Override it in `.env` or in the shell with `BASE_URL` when pointing at another compatible service.

## Run tests

Fast mocked tests:

```powershell
& .\.venv\Scripts\python.exe -m pytest -q
```

BDD dry run, which validates feature and step wiring without network calls:

```powershell
& .\.venv\Scripts\behave.exe --dry-run
```

Live API suite:

```powershell
& .\.venv\Scripts\behave.exe
```

The live scenarios generate a unique email for each run. Created users are deleted by the Behave scenario hook, including after failed scenarios where possible.

## Allure reporting

`allure-behave` creates the result files; the `allure` command itself is a separate CLI and requires Java. Install both once on Windows:

```powershell
winget install EclipseAdoptium.Temurin.17.JDK --source winget
npm install --global allure-commandline
```

Close and reopen PowerShell after installation, then verify:

```powershell
java -version
allure.cmd --version
```

Generate Allure result files while running Behave:

```powershell
& .\.venv\Scripts\behave.exe -f allure_behave.formatter:AllureFormatter -o allure-results
allure.cmd serve allure-results
```

On PowerShell systems that block `.ps1` scripts, use `allure.cmd` exactly as shown above. If a new terminal still cannot find Java, restart PowerShell so it reloads the updated user `JAVA_HOME` and PATH values.

## API coverage

| Capability | Method | Endpoint |
| --- | --- | --- |
| Create account | POST | `/api/createAccount` |
| Verify login | POST | `/api/verifyLogin` |
| Get user detail | GET | `/api/getUserDetailByEmail` |
| Update account | PUT | `/api/updateAccount` |
| Delete account | DELETE | `/api/deleteAccount` |
