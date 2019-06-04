FROM python

ENV TERM=xterm
RUN pip install requests
RUN pip install mysql-connector-python