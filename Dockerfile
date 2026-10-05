FROM python:3.12

WORKDIR /app

RUN printf '#!/bin/bash\n\
python app.py' > /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
    
COPY . /app

EXPOSE 8532
ENTRYPOINT ["bash", "/entrypoint.sh"]
