# Campus Events Booking Website

Campus Events is a small Python web application that displays upcoming events and allows visitors to reserve places. Each successful booking receives a reference number, and the number of available places is updated.

## Requirements

Python 3.10 or later. The application uses only the Python standard library; no additional packages are required.

## Run the website

From the project folder, run:

```text
python app.py
```

Open http://127.0.0.1:5000 in a browser. Use fictional names when testing bookings. Press Ctrl+C in the terminal to stop the server.

## Check the application

```text
python scripts/check_app.py
```

## Package a release

```text
python scripts/build_release.py
```

The generated release ZIP is saved in `dist/`. Extract the ZIP and run `python app.py` from its `campus-events` folder to launch that release independently.

## Local data

Bookings are stored in `instance/bookings.sqlite3`. The `instance/` directory is excluded from version control and release packages. This is a local classroom application, not a production booking service; do not enter real personal information or expose it publicly.
