from django.db import transaction


class BaseRepository(object):


    def begin_transaction(self):
        transaction.set_autocommit(False)


    def commit_transaction(self):
        transaction.commit()
        transaction.set_autocommit(True)


    def rollback_transaction(self):
        transaction.rollback()
        transaction.set_autocommit(True)