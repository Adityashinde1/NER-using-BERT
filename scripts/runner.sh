api:
    auth_token: AUTH_TOKEN

runner:
    name: self-hosted
    working_directory: /var/opt/circleci/workdir
    cleanup_working_directory: true

[Unit]
Description=CircleCI Runner
After=network.target
[Service]
ExecStart=/opt/circleci/circleci-launch-agent --config /etc/opt/circleci/launch-agent-config.yaml
Restart=always
User=circleci
NotifyAccess=exec
TimeoutStopSec=18300
[Install]
WantedBy = multi-user.target