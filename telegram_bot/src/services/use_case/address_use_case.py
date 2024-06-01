from typing import List

from src.core.settings import DefaultSettings
from src.services.interface import AbstractAddressRepository
from src.services.entities import AddressEntity


class AddressService:

    def __init__(self,
                 config: DefaultSettings,
                 address_repo: AbstractAddressRepository) -> None:
        self.config = config
        self.address_repo = address_repo

    async def get_all_addresses(self) -> List[AddressEntity]:
        return await self.address_repo.find_all()

    async def add_new_address(self, data: AddressEntity) -> int:
        address = await self.address_repo.add(data)
        return address.id

    async def get_address_info(self, address_id: int):
        address_info = await self.address_repo.get_address_detail(address_id)
        return address_info
