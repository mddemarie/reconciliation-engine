# Reconciliation Engine App

The goal of the exercise is to build the “Reconciliation Engine” service.

The service will expose an API, with the payment data as a json input object, and the engine will return the possibly related business transactions.

## SETUP

I assume you already installed Python 3.4 or higher and pip.

### Virtual Environment

Install virtualenv via pip:

```
$ pip install virtualenv
```

Create a virtual environment for a project:

```
$ cd this-project
$ virtualenv env
```

To use the virtual environment, you can activate it with:

```
$ source env/bin/activate
```

### Installation

Install the project packages including Django:

```
(venv) $ pip install -r requirements.txt
```

##### On Mac

Install GraphiQL - GUI for editing and testing GraphQL queries and mutations:

```
brew cask install graphiql
```

