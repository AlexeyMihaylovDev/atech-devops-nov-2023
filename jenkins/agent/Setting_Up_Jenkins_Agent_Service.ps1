# Jenkins Agent parameters
$jenkinsUrl = "http://localhost:8088/"
$agentSecret = "f45348ef7a10c9edbdab8a0f224474650f9b901aaa682bb2d174f2112c62f9b2"
$agentName = "win"
$workDir = "F:\win_agent"
$winSWUrl = "https://github.com/winsw/winsw/releases/download/v2.11.0/WinSW-x64.exe"
$winSWExe = "$workDir\jenkins-agent.exe"
$agentJar = "$workDir\agent.jar"
$xmlConfigPath = "$workDir\jenkins-agent.xml"

# Create the working directory
if (-Not (Test-Path -Path $workDir)) {
    New-Item -Path $workDir -ItemType Directory
}

# Download WinSW (Windows Service Wrapper)
Invoke-WebRequest -Uri $winSWUrl -OutFile $winSWExe

# Download agent.jar from Jenkins
Invoke-WebRequest -Uri "$jenkinsUrl/jnlpJars/agent.jar" -OutFile $agentJar

# Create XML configuration for WinSW
$xmlContent = @"
<service>
  <id>jenkins-agent</id>
  <name>Jenkins Agent</name>
  <description>This service runs Jenkins agent.</description>
  <executable>java</executable>
  <arguments>-jar "$agentJar" -url $jenkinsUrl -secret $agentSecret -name $agentName -workDir "$workDir"</arguments>
  <logmode>rotate</logmode>
</service>
"@
$xmlContent | Set-Content -Path $xmlConfigPath

# Install and start Jenkins Agent service
& $winSWExe install
& $winSWExe start

Write-Host "Jenkins Agent has been installed as a service and started."

