from metal.models.MasterData import Supplier
from metal.business.repository.repo_base import BaseRepository


class SupplierRepository(BaseRepository):

    def register_supplier(self, user_profile, tags):
        supplier = Supplier(
            User_Profile=user_profile,
            MServiceTags=tags,
            Total_SubmittedQuotes=0,
            Total_QuotesWon=0,
            Total_QuotesMissed=0
        )
        supplier.save()
        return supplier

