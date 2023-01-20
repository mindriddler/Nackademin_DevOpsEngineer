# Exercise 5

## Instructions

Use the image from the classroom lab for Dockerfile & docker flask <https://classroom.github.com/a/kYYrYrGm>

### Push to GitHub Container Registry

In this exercise we will push a docker image to a GitHub Container Registry. We will later use this registry to download the docker image used in the deploy on minikube. Read more about [Working with the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)

1. Before you start with this part, your should complete the classroom lab. It will create a repository from the template [python-dockerfile-flask](https://github.com/nackademin-devops22/python-dockerfile-flask)
2. Create another private repository in your personal GitHub account [how to](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), name it `my_container_registry`
3. Create a `personal access token` in your private repository my_container_registry with the scopes `read:packages` and `write:packages`. [how to](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
4. To be able to push a image to your docker container registry, you must first login your docker client. In your terminal of choice, login with your personal access token:

    ```bash
    docker login ghcr.io -u USERNAME
    ```

    When you copy the password, make sure to copy exactly the password/token, if it doesn't work, try to paste with ctr+shift+v on windows to avoid formatting.

5. Before you may push the container image, it needs to be tagged/built with the full repository url. In your classroom project root, next to the Dockerfile. You can build with the command docker:

    ```bash
    build -t ghcr.io/YOUR_USERNAME/my_container_registry/my_image . 
    ```

    or if you already built it with another name you can tag it again. Find your image-id with:

    ```Bash
    docker image ls
    # then tag with
    docker tag <image-id> ghcr.io/YOUR_USERNAME/my_container_registry/my_image .
    ```

6. Push your container to the container registry with the command:

    ```bash
    docker push ghcr.io/YOUR_USERNAME/my_container_registry/my_image
    ```

7. Verify that your push worked in the terminal then also inspect the `https://github.com/YOUR_USERNAME?tab=packages`

## Hand in instructions

No hand in this exercise. But we will use your work next lesson.
