from pydantic import BaseModel


class Language(BaseModel):
    START_MESSAGE: str
    HELP_MESSAGE: str
    ADDRESS_MESSAGE: str
    ADDRESS_INFO_MESSAGE: str
    ADDRESS_CAR_MESSAGE: str
    ADDRESS_CAMERA_CONFIG_MESSAGE: str
    ADDRESS_ADD_CAR_NUMBER: str

    CAMERA_CONFIG_BUTTON: str

    ADDRESSES: str
    CAR_NUMBERS: str
    CAMERAS_CONFIG: str
    ADD_ADDRESS: str
    DEL_ADDRESS: str
    EDIT_ADDRESS: str
    INPUT_ADDRESS: str
    APPEND_ADDR_ERROR: str
    APPEND_ADDR_SUCCESSFUL: str
    BACK: str
