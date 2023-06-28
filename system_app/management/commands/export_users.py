import os
import json
import zipfile

from django.core.management.base import BaseCommand
from django.conf import settings

from system_app.models import User

class Command(BaseCommand):
    help = 'Export users and related files as separate ZIP archives.'

    def handle(self, *args, **options):
        # Recupera todos os usuários
        users = User.objects.all()

        for user in users:
            # Cria um dicionário com os dados do usuário
            user_data = {
                'nome': user.nome,
                'idade': user.idade
            }

            # Cria o nome do arquivo ZIP
            zip_filename = f'{user.nome}_data.zip'
            zip_path = os.path.join(settings.MEDIA_ROOT, zip_filename)

            # Cria o arquivo ZIP
            with zipfile.ZipFile(zip_path, 'w') as zip_file:
                
                # Pega o caminho base dos arquivos, mas sem salvar a hierarquia de pastas
                foto_filename = os.path.basename(user.foto.path)
                curriculo_filename = os.path.basename(user.curriculo.path)
                
                # Cria um arquivo JSON com os dados do usuário
                json_filename = f'{user.nome}.json'
                json_path = os.path.join(settings.MEDIA_ROOT, json_filename)

                with open(json_path, 'w') as json_file:
                    json.dump(user_data, json_file)

                # Adiciona o arquivo JSON ao arquivo ZIP
                zip_file.write(json_path, arcname=json_filename)
                os.remove(json_path)

                # Adiciona a foto do usuário ao arquivo ZIP
                zip_file.write(user.foto.path, arcname=foto_filename)

                # Adiciona o currículo do usuário ao arquivo ZIP
                zip_file.write(user.curriculo.path, arcname=curriculo_filename)

        self.stdout.write(self.style.SUCCESS('Successfully exported users to separate ZIP archives.'))