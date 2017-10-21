from metal.models.MasterData import Buyer
from metal.business.repository.repo_base import BaseRepository


class BuyerRepository(BaseRepository):

    def register_buyer(self, user_profile):
        buyer = Buyer(
            User_Profile=user_profile,
            Rfq_Count = 0,
            Total_Closed_Rfq_Count = 0,
            Total_Withdraw_Rfq_Count = 0,
            Total_Award_Rfq_Count = 0
        )
        buyer.save()
        return buyer

