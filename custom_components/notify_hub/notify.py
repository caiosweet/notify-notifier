"""HUB notifications based on AppDaemon."""
import logging

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.notify import ATTR_DATA, PLATFORM_SCHEMA, BaseNotificationService

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'notify_hub'


def get_service(hass, config, discovery_info=None):
    """Get the notification service."""
    return NotifyHub()


class NotifyHub(BaseNotificationService):

    def send_message(self, message="", **kwargs):
        """Send a message."""
        data = {}
        if kwargs.get(ATTR_DATA) is not None:
            data = kwargs.get(ATTR_DATA)
        data['message'] = message
        data['title'] = kwargs.get('title', '')
        data['target'] = kwargs.get('target', '')
        data['alexa'] = data.get('alexa', '')
        data['called_number'] = data.get('called_number', '')
        data['caption'] = data.get('caption', '')
        data['file'] = data.get('file', '')
        data['google'] = data.get('google', '')
        data['html'] = data.get('html', '')
        data['link'] = data.get('link', '')
        data['location'] = data.get('location', '')
        data['no_show'] = data.get('no_show', '')
        data['notify'] = data.get('notify', '')
        data['priority'] = data.get('priority', '')
        data['url'] = data.get('url', '')
        self.hass.bus.fire("hub", data) #hass.bus.async_fire
        _LOGGER.debug(f"\n\nHUB: {data} \n\n kwargs: {kwargs}")