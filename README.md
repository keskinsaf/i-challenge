# I - Challenge Solution

This project contains solution created for the 
[case](https://gist.github.com/aeroith/16b9549659aab23fc9335dce7f749f0d).

In this project, a RESTful API created with single endpoint. According to explanations,
when a request is received by that endpoint, an identicon similar to 
[GitHub's approach](https://github.blog/2013-08-14-identicons/) is generated and returned
to the client.

Project is completed in [Python 3.6](https://www.python.org/downloads/release/python-368/), and tested with both 
[Python 3.6,8](https://www.python.org/downloads/release/python-368/) and 
[Python 3.6.10](https://www.python.org/downloads/release/python-3610/).

[Flask](https://www.palletsprojects.com/p/flask/) web application 
framework is used for handling requests.

[Pillow](https://pillow.readthedocs.io/en/stable/) Python Image Library is used in order 
to generate and operate on image.

[uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/) is used for deployment.

## Dependencies
 - [Flask](https://www.palletsprojects.com/p/flask/)
 - [Pillow](https://pillow.readthedocs.io/en/stable/)
 - [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/)


## Building, Running and Deployment

### Run on Docker (*Recommended for Deployment*)
First, an image should be built with the provided Dockerfile.

```shell script
[sudo] docker build -t i-challenge .
```

Then, you can run api on the docker with the command below.
```shell script
[sudo] docker run --rm -d -p 5000:5000 --name i-challenge i-challenge
```

You can follow logs with command below:
```shell script
[sudo] docker logs -f i-challenge
```

At each request, program will be log some information about incoming request 
and operations performed on the api.

### Run on Virtual Environment (*Recommended for Development*)
Firstly, you should set up a virtual environment. Then, steps mentioned at 
[Run on local machine](#run-on-local-machine-not-recommended) can be followed.

1. Set up virtual environment
```shell script
python3 -m venv [name of the virtual environment]
```

After running command above, a directory with the specified name have been created 
at in the project directory. You can activate that virtual environment with the 
command below:
```shell script
source [virtual env name]/bin/activate
```
After that, you can follow steps at 
[Run on local machine](#run-on-local-machine-not-recommended) section.

### Run on local machine (*Not Recommended*)

1. Ensure that Python 3.6 is installed
    ```shell script
    # python --version
    # or
    python3 --version
    # output: Python 3.[Minor.Patch]
    ```
2. Ensure that pip is installed
    ```shell script
    # pip --version
    # or
    pip3 --version
    # output: pip [version] from [pip path] (python 3.[Minor])
    ```
3. Install Flask, Pillow and uwsgi
    ```shell script
   $ pip3 install Flask && pip3 install Pillow && pip3 install uwsgi 
    ```
4.
    1. Run api in Development mode
        ```shell script
        $ flask run
        ```
    2. Run api in Deployment mode
        ```shell script
        $ uwsgi --http :5000 --wsgi-disable-file-wrapper \
           -s /tmp/i-challenge.sock --manage-script-name \
           --mount /=app:app
        ```

## Testing

In order to test that api, get request should be sent to specified url & port 
combination with or without query params.
While testing, [PostMan](https://www.getpostman.com/) 
and [curl](https://curl.haxx.se/) are used.

Some test options are listed below.

- http://localhost:5000/serhat.png?size=300&row=5
- http://localhost:5000/keskinsaf.png
- http://localhost:5000/somename.png?size=200
- http://localhost:5000/username.png?row=3
- http://localhost:5000/username.png?row=1
- http://localhost:5000/somebody.png?row=1&size=400