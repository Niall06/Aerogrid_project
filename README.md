AeroGrid Turbine Telemetry Analysis
This repository contains an automated data processing and visualization pipeline for AeroGrid's turbine network. Built using Python and Pandas, the script ingests raw telemetry data, detects anomalies against engineering thresholds, and automatically generates individual diagnostic plots for every turbine. The environment is fully containerized using Docker.

How to Run via Docker:

Ensure Docker Desktop is installed and running.

Build the container image: docker build -t aerogrid-app . 

Run the container: docker run aerogrid-app (Note: As this is an isolated container, execution outputs are processed securely inside the container's temporary file system.)

