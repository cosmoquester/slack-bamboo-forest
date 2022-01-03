# Slack Bamboo Forest

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![cosmoquester](https://circleci.com/gh/cosmoquester/slack-bamboo-forest.svg?style=svg)](https://app.circleci.com/pipelines/github/cosmoquester/slack-bamboo-forest)

This is simple flask server receving messages from user to forwarding specific channel ananymously.

## Slack

- channels:read
- chat:write
- im:history
- im:read

Slack bamboo forest app require upper bot permission scopes.

You should activate `Message Tab` and allow user to send message to bot.

Lastly, you should enable event and set `message.im` event subscription.
