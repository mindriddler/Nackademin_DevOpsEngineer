# Python in Docker

## Run flask manually without docker

1. Create & activate a virtual environment
2. Run `pip install -r requirements.txt`
3. Try to start the server with:

    ```bash
    # On linux/mac
    FLASK_APP=hello_flask flask run
    ```

    ```pwsh
    # On windows powershell
    $env:FLASK_APP="hello_flask"
    flask run
    ```

4. The flask server will print a url that you can open in a browser
5. Shutdown your flask server to release the port 5000

## Run flask with docker

### Docker

Docker is one of the most popular OS-level virtualization platforms.

#### Basic commands

* List running containers `docker ps`
* Stop container `docker stop <container name>`
* Start temporary container with port `docker run -p 5000:5000 --rm -it flask`
* Start container as daemon/service (in background) `docker run -p 5000:5000 --rm -d flask`
* Prune images `docker image prune`
* Prune all `docker system prune`

#### Build with Dockerfile

1. In the repository root folder
2. Build the docker image `docker build -t my_flask .`
3. Run a container `docker run -p 5000:5000 --rm -it my_flask`
4. The url printed in the log is inside the docker container. The flag -p 5000:5000 is what opens <http://localhost:5000> targeting the container port 5000. If your system can't open the port 5000 it most probably already has a flask running in another terminal.
