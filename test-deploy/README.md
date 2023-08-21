## Usage

Requires: Docker Compose

1. Clone this repository.
2. Ensure that the Docker daemon is running (for example, by opening Docker Desktop).
3. In your preferred command line interface, navigate to the `ontosheep/test-deploy` directory (within the cloned repository), and then run the command `docker compose run app > results.txt`.  Results will be saved to `results.txt`
4. Once complete, you will also need to stop the triplestore container.  Run the command `docker ps` to get the name, and then run `docker stop <container name>`.
