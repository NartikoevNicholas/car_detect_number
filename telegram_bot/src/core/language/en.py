from .lang import Language


class EN(Language):
    START_MESSAGE: str = "Hi, {0}!\nThis bot need for control your security"
    HELP_MESSAGE: str = 'Helper'
    ADDRESS_MESSAGE: str = ('This section contains your addresses.\n'
                            'Here you can edit or add a new address')
    ADDRESS_INFO_MESSAGE: str = 'Information for address: {0}.'
    ADDRESS_CAR_MESSAGE: str = 'All machine numbers that were recorded'
    ADDRESS_CAMERA_CONFIG_MESSAGE: str = 'Camera configuration'
    ADDRESS_ADD_CAR_NUMBER: str = 'bind car number'

    CAMERA_CONFIG_BUTTON: str = 'Host: {0}. Port: {1}.'

    ADDRESSES: str = 'Addresses'
    CAR_NUMBERS: str = 'Car numbers'
    CAMERAS_CONFIG: str = 'Cameras config'
    ADD_ADDRESS: str = 'Add new address'
    DEL_ADDRESS: str = 'Remove address'
    EDIT_ADDRESS: str = 'Edit address'
    INPUT_ADDRESS: str = 'Input address'
    BACK: str = 'Back'
    APPEND_ADDR_ERROR: str = 'Address not added'
    APPEND_ADDR_SUCCESSFUL: str = 'Address added successfully'
