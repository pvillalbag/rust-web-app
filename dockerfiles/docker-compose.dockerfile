FROM docker/compose:1.23.2
RUN apk --no-cache add curl 
ENTRYPOINT [ "sh", "-c" ]