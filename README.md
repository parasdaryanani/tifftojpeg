# TIFF to JPEG converter

Super simple web app to convert one or more tiff files to jpeg.
### Single mode
Upload a single tiff file and receive a single converted jpeg file.
![Single Mode](img/single-mode.png)
### Batch mode
Upload multiple tiff files and receive a zip file containing converted jpeg files.
![Batch Mode](img/batch-mode.png)

### Run with Docker
```sh
docker build . -t tifftojpeg && docker run tifftojpeg
```

### Credits
Based on https://github.com/kckaiwei/tifftojpeg