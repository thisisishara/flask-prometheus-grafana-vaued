VERSION=0.0.0
docker build -t vaued_app_image:$VERSION -f DockerfileVAUED .
# docker build -t vaued_app_image:0.0.0 -f DockerfileVAUED .
# docker build -t thisisishara/vaued-app:1.0.0 -f DockerfileVAUED .
