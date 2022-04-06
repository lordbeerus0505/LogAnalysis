# Steps to run Prometheus and Grafana on Azure
## Setup on Azure Windows 2019 server
#### Install Chrome using this command on powershell:
$LocalTempDir = $env:TEMP; $ChromeInstaller = "ChromeInstaller.exe"; (new-object    System.Net.WebClient).DownloadFile('http://dl.google.com/chrome/install/375.126/chrome_installer.exe', "$LocalTempDir\$ChromeInstaller"); & "$LocalTempDir\$ChromeInstaller" /silent /install; $Process2Monitor =  "ChromeInstaller"; Do { $ProcessesFound = Get-Process | ?{$Process2Monitor -contains $_.Name} | Select-Object -ExpandProperty Name; If ($ProcessesFound) { "Still running: $($ProcessesFound -join ', ')" | Write-Host; Start-Sleep -Seconds 2 } else { rm "$LocalTempDir\$ChromeInstaller" -ErrorAction SilentlyContinue -Verbose } } Until (!$ProcessesFound)
#### Install prometheus
Download it from `https://github.com/prometheus/prometheus/releases/download/v2.34.0/prometheus-2.34.0.windows-amd64.zip`  
Alter the contents of the prometheus.yml file after extraction.
#### Download and install grok exporter
Alter contents of patterns/custom-logs , example/config.yml
Add the log-server directory and the server.log file
Also alter contents of the config file to change input path to this server.log file.
#### Start the prometheus server and the grok server and grafana
prometheus.exe
grok_exporter.exe -config example\config.yml
nssm start grafana
#### Start the server and client
python server.py
python client.py after conda activate sml