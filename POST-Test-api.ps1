$headers = @{
    "Content-Type" = "application/json"
}

$body = @{
    "features" = @(298.2, 308.7, 1408, 40.0, 9, 1, 0, 0, 0, 0, 0, 0)
} | ConvertTo-Json -Depth 1

Invoke-RestMethod -Uri "http://localhost:8000/predict" -Method Post -Headers $headers -Body $body