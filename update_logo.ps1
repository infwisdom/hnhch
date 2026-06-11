$files = @("index.html", "about.html", "facilities.html", "worship.html", "ministry.html", "next_gen.html", "directions.html")
$target = '<a href="index.html" class="logo">해남성결교회</a>'
$replacement = '<a href="index.html" class="logo">
                <img src="assets/교회로고.png" alt="해남성결교회">
            </a>'

foreach ($file in $files) {
    try {
        $path = Join-Path "c:\Users\Pastor Y\Desktop\홈페이지" $file
        if (Test-Path $path) {
            $content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
            if ($content.Contains($target)) {
                $newContent = $content.Replace($target, $replacement)
                [System.IO.File]::WriteAllText($path, $newContent, [System.Text.Encoding]::UTF8)
                Write-Host "Updated $file"
            } else {
                Write-Host "Skipped $file (Target not found)"
            }
        }
    } catch {
        Write-Host "Error processing $file`: $_"
    }
}
