import logging
from homeassistant.components.light import ...   # Update this line, removing ATTR_COLOR_TEMP

# ... other imports

async def async_turn_on(self, **kwargs):
    # Other logic here
    # Remove the following line
    # color_temp = kwargs.get(ATTR_COLOR_TEMP, 261)
    
    # Additional code logic

# Continue with the implementation