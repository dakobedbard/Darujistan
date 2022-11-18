import Keycloak from "keycloak-js";
const keycloak = new Keycloak({
 url: "http://keycloak:3005",
 realm: "daru-realm",
 clientId: "daru-client",
});

export default keycloak;