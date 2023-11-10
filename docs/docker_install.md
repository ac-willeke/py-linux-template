### Install Docker Image

```bash
# pull image from docker hub repository
docker pull osgeo/gdal:ubuntu-small-latest

# create the container and enter it
docker run -it osgeo/gdal:ubuntu-small-latest

root@<container-id>:/#
```

### Check the pre-installed package versions in the image

```bash
root@049c755ca6ff:/# python
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import gdal
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'gdal'
>>> from osgeo import gdal
>>> gdal.__version__
'3.7.0dev-8ec21bbf7073f9105a2b4bf70adb6dce0d295874'
# exit python
>>> exit()
```

```bash
# exit docker container
root@049c755ca6ff:/# exit
```


### Create Dockerfile which install sadditional packages

**pip, pipx, poetry**
See docker file

## Build image
```bash
# build docker image
docker build .
docker build -t <image-name>:<image-tag> .

# list docker images
docker images

# enter docker image
docker run -it <image-id>

# remove docker image
docker rmi <image-id>
```

# Build, run and debug container in VS Code


## Enter Docker image in VS Code

Open VS code in container
1. CTRL + SHIFT + P
2. Dev Contains: Reopen Folder in container ...
3. Select Project Folder
4. Select Additional Features (optional)

Add VS Code Extensions in container

Close container in VS code
1. CTRL + SHIFT + P
2. Dev Contains: Reopen Folder locally ...
