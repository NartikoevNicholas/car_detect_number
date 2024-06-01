from .lang import Language


class RU(Language):
    START_MESSAGE: str = "Привет, {0}!\nЭтот бот нужен для контроля вашей безопасности"
    HELP_MESSAGE: str = 'Помощник'
    ADDRESS_MESSAGE: str = ('В этом разделе находятся ваши адреса.\n'
                            'Тут можно отредактировать или добавить новый адрес')
    ADDRESS_INFO_MESSAGE: str = 'Информация по адресу: {0}.'
    ADDRESS_CAR_MESSAGE: str = 'Все машинные номера, которые удалось зафиксировать'
    ADDRESS_CAMERA_CONFIG_MESSAGE: str = 'Конфигурация камеры'
    ADDRESS_ADD_CAR_NUMBER: str = 'Привязать номер машины'

    CAMERA_CONFIG_BUTTON: str = 'Хост: {0}. Порт: {1}.'

    ADDRESSES: str = 'Адресы'
    CAR_NUMBERS: str = 'Номера машин'
    CAMERAS_CONFIG: str = 'Настройки камер'
    ADD_ADDRESS: str = 'Добавить новый адрес'
    DEL_ADDRESS: str = 'Удалить адрес'
    EDIT_ADDRESS: str = 'Редактировать адрес'
    INPUT_ADDRESS: str = 'Введите адрес'
    APPEND_ADDR_ERROR: str = 'Адрес не добавлен'
    APPEND_ADDR_SUCCESSFUL: str = 'Адрес успешно добавлен'
    BACK: str = 'Назад'

