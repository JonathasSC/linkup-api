# Usar a imagem Python oficial como base
FROM python:3.10-alpine

# Configurações do Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Definir o diretório de trabalho
WORKDIR /api

# Instalar dependências
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar os arquivos da aplicação
COPY . /api/

# Expor a porta 8000 (caso precise ser acessada diretamente)
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE=core.settings.production
# Comando para iniciar o servidor Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
