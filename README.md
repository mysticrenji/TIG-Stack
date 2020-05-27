# Latency test with TIG-Stack

## 1. Latency Test
We can simulate latency test using latencytest.sh file. The script can be run with different arguments (low, medium , high ranges)

> latencytest.sh medium


none     = no latency change </br>
low    = 100 ms </br>
medium   = 500 ms </br>
high   = 1000 ms </br>
show   = Current latency profile </br>

## 2. TIG stack using Docker Compose
Docker compose file comprises of Telegraf, InfluxDB and Grafana. The default credentials are preconfigured </br>
Influx DB will be hosted in port 8086 </br>
Grafana will be hosted in port 3000 </br>

Telegraf config has additional input plugins than the default one that comes along with the package</br>
you may find it in the below path </br>
> /docker-influxdb-grafana/telegraf.conf </br>

>[[inputs.ping]] </br>
>interval = "60s" </br>
>urls = ["208.67.222.222", "208.67.220.220", "ddg.gg", "pfSense.home", "accessPoint.home", "amazon.com", "github.com"] </br>
>count = 4 </br>
>ping_interval = 1.0 </br>
>timeout = 2.0 </br>

I have used Internet Bandwidth Monitor dasboard to visualise the latency by importing Dashboard Template. Dashboard ID - 2690

You may start the process by running run.sh </br> </br>
>run.sh


![Internet Bandwidth Dashboard](https://github.com/mysticrenji/TIG-Stack/blob/master/Internet%20bandwidth%20Monitor.PNG)
