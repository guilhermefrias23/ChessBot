from django.core.management.base import BaseCommand
from django.conf import settings


from apps.chess_bot.support_scripts.import_chess import ImportBoard


class Command(BaseCommand):

    def handle(self, *args, **options):


        x = ImportBoard.CreateBoard()
        print(x)

        print("uma nova cena")
        print("new")

