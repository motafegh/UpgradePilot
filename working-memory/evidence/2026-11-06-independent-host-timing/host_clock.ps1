# Trusted local observer only. Input lines are protocol verbs, never executable text.
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding($false)
$session = [System.Diagnostics.Stopwatch]::StartNew()
$interval = New-Object System.Diagnostics.Stopwatch
function Emit-Clock([string]$Operation) {
    $packet = @{
        op = $Operation
        frequency = [System.Diagnostics.Stopwatch]::Frequency
        high_resolution = [System.Diagnostics.Stopwatch]::IsHighResolution
        qpc_timestamp = [System.Diagnostics.Stopwatch]::GetTimestamp()
        utc_ticks = [DateTime]::UtcNow.Ticks
        session_ticks = $session.ElapsedTicks
        elapsed_ticks = $interval.ElapsedTicks
        running = $interval.IsRunning
    }
    [Console]::Out.WriteLine(($packet | ConvertTo-Json -Compress))
    [Console]::Out.Flush()
}
Emit-Clock 'ready'
while ($null -ne ($verb = [Console]::In.ReadLine())) {
    switch ($verb) {
        'begin' {
            if ($interval.IsRunning) { throw 'Interval already running.' }
            $interval.Restart()
            Emit-Clock 'begin'
        }
        'sample' { Emit-Clock 'sample' }
        'end' {
            if (-not $interval.IsRunning) { throw 'No running interval.' }
            $interval.Stop()
            Emit-Clock 'end'
        }
        'quit' { Emit-Clock 'quit'; return }
        default { throw 'Unknown clock protocol verb.' }
    }
}
