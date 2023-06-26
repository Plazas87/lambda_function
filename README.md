# Galeo Lambda function

## Prerequisites

Before messing up with the code get yourself ready with all the tooling needed, otherwise you will end up crying and pulling your hair out.

1. Python ^3.10
2. [Poetry](https://python-poetry.org)

__Tip__: If you need to manage different python versions, I would recommend you to use [pyenv](https://github.com/pyenv/pyenv) 

Choose the python version desired and install it, for example:
```bash
pyenv install 3.10.7
```

## Installation

To install project dependencies execute the following commands:

```bash
poetry install
```

### Build the Lambda function image to use it locally

This time, were are not going to deploy the lambda function. We are going
to deploy it locally and test it. For this, first, we you need to build the Docker image.

```bash
docker build -t galeo-lambda .
```

## Usage

The Lambda function deployed locally work almost the same as a lambda function running in AWS. 
By running it locally, we can test its behavior together with other components, in this case, a NoSQL database. 

This challenge ask for saving the processed data into DynamoDB which is NoSQL AWS database, but in order to be able to test the processing process (a very very simple one) and the data saving process, we are going to use a MongoDB instance(or DocumentDB in AWS), which is also a NoSQL database, to save the data.



### Lambda function invokation example
```bash
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"body": {"data": [{...}]}}'  
```
Here we are going to replace '[{...}]' with fake temperature data in a json format.

For, example:
```python
[{"temperature": "27"}, {"temperature": "31"}, {"temperature": "36"}, ...]  
```

{"body": {"data": [{"temperature": "27"}, {"temperature": "31"}, {"temperature": "36"}]}}

