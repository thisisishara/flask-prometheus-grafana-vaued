# flask_prometheus_grafna_vaued
VAUED Assignment 2 Implementation: A Grafana dashboard to monitor Flask app using Prometheus

### Port Mappings

| Service Name      | URL                   |
|-------------------|-----------------------|
| Prometheus        | http://localhost:9090 |
| VAUED-App (Flask) | http://localhost:9091 |
| Grafana           | http://localhost:9092 |

### Deployment
1. Clone the repository (main / release)
2. Run `docker-compose build` to build the flask image
3. Run `docker-compose up -d` to run all servers detached
4. Run `docker-compose logs` for troubleshooting
5. Run `docker-compose down` to take down the services
  
  
### Metrics Endpoints

| Service Name      | URL                           |
|-------------------|-------------------------------|
| VAUED-App Metrics | http://localhost:9091/metrics |
| Docker Metrics    | http://localhost:9323/metrics |
  
  
### Dashboards

| Dashboard Name        | Content                                                 |
|-----------------------|---------------------------------------------------------|
| FlaskPerformanceWatch | Visualizations related to flask server performance      |
| FlaskEndpointWatch    | Visualizations related to flask endpoint stats          |
| DockerContainerWatch  | Visualizations related to the docker daemon of the Host |
| DockerEngineWatch     | Visualizations related to the docker engine of the Host |
  
  
### Team Members

| IT Number  | Name                   | GitHub Username                                                   |
|------------|------------------------|-------------------------------------------------------------------|
| IT19051208 | Sakalasooriya S.A.H.A. | [akalankasakalasooriya](https://github.com/akalankasakalasooriya) |
| IT19075754 | Jayasinghe D.T.        | [dinushiTJ](https://github.com/dinushiTJ)                         |
| IT19045986 | De Silva N. N. M       | [Nithya980711](https://github.com/Nithya980711)                   |
| IT19069432 | Dissanayake D.M.I.M.   | [thisisishara](www.github.com/thisisishara)                       |
