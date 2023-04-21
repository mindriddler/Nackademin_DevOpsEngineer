#!/bin/bash

expectupdates() {
    expect <<EOF
  spawn yay -Syu
  expect_background -ex "Proceed with installation" {send "n"}
  interact
EOF
}
$expectupdates
ethernet_link=$(ip link show | grep -e 'state UP' | cut -d ':' -f2)
ethernet_link_status=$(ip link show $ethernet_link | head -1 | head -1 | cut -d ' ' -f3 | cut -d '<' -f2 | cut -d '>' -f1)
default_router_ip=$(ip route show default dev ${ethernet_link} | cut -d ' ' -f3)
default_router_ping_time=$(ping $default_router_ip -c 3 -q | tail -n1 | cut -d '/' -f 5)
tcp_connections=$(ss -tn | tail -n +3 | wc -l)
zsh_files=$(lsof -c zsh | wc -l)
pkg_manager=""
yay="yay"*
yay_installed=$(pacman -Qe | grep "yay")
if [[ "$yay_installed" == $yay ]]; then
    echo "you got yay installed, so no sudo is nessecery"
    pkg_manager="yay"
else
    echo "you dont have yay installed, so sudo is nessecery"
    pkg_manager="sudo pacman"
fi

echo "
<html>
<head>
<title>Report</title>
</head>
<body>
<h1>System information</h1>
<h2>Hostname: $(hostname)</h2>
<h2>User running report: $USER</h2>
<h2>Report running date: $(date)</h2>
<h2>Uptime: $(uptime -p)</h2>
<h2>Installed packages: $($pkg_manager -Qe | wc -l)</h2>
<h2>Upgradable packages: $($pkg_manager -Qu | wc -l)</h2>
<h2>Ping: $default_router_ping_time ms</h2>
<h2>Internet connection: $ethernet_link_status</h2>
<h2>Number of TCP connections: $tcp_connections</h2>
<h2>Number of file which zsh has opened: $zsh_files
</body>
</html>

" >/home/mindriddler/index.html
