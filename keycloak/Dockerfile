FROM quay.io/keycloak/keycloak:18.0.2

USER root

COPY entrypoint.sh /usr/local/bin/
RUN ["chmod", "+x", "/usr/local/bin/entrypoint.sh"]

USER 1000
ENTRYPOINT ["sh", "/usr/local/bin/entrypoint.sh"]
