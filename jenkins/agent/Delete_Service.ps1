$serviceName = 'jenkins-agent'
try {
  $service = Get-Service -Name $serviceName -ErrorAction Stop
  if ($service.Status -ne 'Stopped') {
    Stop-Service -Name $serviceName -Force
  }
  sc.exe delete $serviceName
  Write-Host "Service '$serviceName' has been deleted successfully."
} catch {
  Write-Host "Error: $_"
}