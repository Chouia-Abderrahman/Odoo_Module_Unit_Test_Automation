# Odoo Module Unit Test Automation with GitHub Actions

This repository demonstrates how to set up a GitHub Action to automatically run unit tests for custom Odoo modules on each push to the `master` branch. The repository contains a nested Odoo project that includes custom modules for testing purposes.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [GitHub Actions Workflow](#github-actions-workflow)
- [Usage](#usage)

## Introduction

Automating the testing process ensures that the code remains reliable and that new changes do not introduce bugs. This repository sets up a GitHub Actions workflow to run unit tests for Odoo custom modules automatically.

## Features

- Automated testing using GitHub Actions.
- Runs tests on every push to the `master` branch.
- Provides a structure for integrating and testing Odoo custom modules.

## GitHub Actions Workflow

The GitHub Actions workflow is defined in `.github/workflows/test.yml`. This workflow performs the following steps:

1. **Checkout the repository**: Fetches the latest code from the repository.
2. **Set up Python environment**: Installs Python and required dependencies.
3. **Install Odoo**: Sets up Odoo and installs the necessary modules.
4. **Run unit tests**: Executes the unit tests for the custom module.

## Usage
To use this repository for your own Odoo projects, simply copy the [workflow file](.github/workflows/test.yml) and customize it to fit your project's requirements.


