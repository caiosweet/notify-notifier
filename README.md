# notify-notifier

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

In your `configuration.yaml` file type:

```yaml

notify:
  - platform: notify_hub
    name: me
```

###### CONFIGURATION VARIABLES

```
  name:
    description: The name of the notify service.
    required: true
    type: string
```

###### Examples

```yaml

notify:
  - platform: notify_hub
    name: hub
```

###### Send text message with TTS
```yaml
service: notify.hub
data: 
  title: Title from Notify Notifier
  message: message da notifier
  data:
   alexa: true
   google:
     volume: 0.5
     message_tts: Hi, from google.
```

###### Send only audio TTS. (equal to notify: 0)
```yaml
service: notify.hub
data: 
  message: ""
  data:
   alexa:
     message_tts: Hello, from Alexa
     volume: 0.3
   google:
     message_tts: Hi, from google.
```
