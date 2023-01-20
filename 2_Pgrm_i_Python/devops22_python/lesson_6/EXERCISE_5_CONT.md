# Exercise 5 Continuation

## Instructions

1. Before you continue, make sure minikube is running:

    ```bash
    minikube status
    ```

2. In GitHub, make sure your image has been uploaded to the GitHub Container Registry `https://github.com/YOUR_USERNAME?tab=packages`

### Add Docker Secret to minikube

We have previously pushed a docker image to GitHub Container Registry. We will now use this registry to download the docker image used in the deploy on minikube.

1. Create another Personal Access Token (Classic) for minikube with the scope `read:packages`, you can note it as `minikube_registry_token`. Why we create another token is because of `The principle of least privilege`, minikube only needs to read.
2. Create a secret for the private container registry in your minikube cluster:

   ```bash
   minikube kubectl -- create secret docker-registry regcred --docker-server=ghcr.io --docker-username="<GitHub username>" --docker-password="<GitHub token>"
   ```

3. Verify that the secret is created:

   ```bash
   minikube kubectl -- get secrets

   # You can also see it as yaml with
   minikube kubectl -- get secrets -o yaml

   # The token is in the base64 encoded the field
   minikube kubectl -- get secrets -o jsonpath='{.items[].data.\.dockerconfigjson}'
   ```

4. Modify the image property in the example `lesson_6/k8s/pod.yml` so it match your GitHub container registry url, save and apply it with:

   ```bash
   minikube kubectl -- apply -f lesson_6/k8s/pod.yml
   ```

5. Verify that the pod is created:

   ```bash
   minikube kubectl -- get pods
   ```

6. Create a port-forward and make sure it works in your browser:

   ```bash
   minikube kubectl -- port-forward pod/my-image :5000
   ```

   The command will run in the foreground, so don't close it down. It will also print which port it opened, e.g `Forwarding from 127.0.0.1:50305 -> 5000` means that you should open `127.0.0.1:50305` in your browser to visit port 5000 in the pod.

## Hand in instructions

1. Demo the running pod for the teacher
2. Delete the running pod `minikube kubectl -- delete -f lesson_6/k8s/pod.yml`
3. Shutdown your minikube cluster `minikube stop`
