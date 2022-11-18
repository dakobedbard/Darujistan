import { useKeycloak } from '@react-keycloak/web'


import Keycloak from "keycloak-js";
export default () => {
  // Using Object destructuring
//   const { keycloak, initialized } = useKeycloak()

  // Here you can access all of keycloak methods and variables.
  // See https://www.keycloak.org/docs/latest/securing_apps/index.html#javascript-adapter-reference
    const url = "http://keycloak:3005/auth" 
  const keycloak = new Keycloak(
      {
    url: url,
    realm: "daru-realm",
    clientId: "daru-client",
   });
   keycloak.init(
       {
        onLoad: 'login-required',
        checkLoginIframe: false,
        redirectUri: 'http://localhost:8080/'
       }
   )
//    keycloak.init(
//        { 
//         onLoad: 
//        'login-required' 
//     }
//     ).then(function(authenticated) {
//         alert(authenticated ? 'authenticated' : 'not authenticated');
//         }).catch(function() {
//             console.log('DFDAFA');
//             alert('failed to initialize ', url);
//         });    



  return (
    <div>
      <div>{`User is ${
        !keycloak.authenticated ? 'NOT ' : ''
      }authenticated`}</div>

      {!!keycloak.authenticated && (
        <button type="button" onClick={() => keycloak.logout()}>
          Logout
        </button>
      )}
    </div>
  )
}

// import React from "react";
// import Keycloak from "keycloak-js";

// const Nav = () => {
//     const keycloak = new Keycloak({
//     url: 'http://keycloak:3005/auth',
//     realm: 'daru-realm',
//     clientId: 'daru-client'
//     });
    // keycloak.init({
    //     onLoad: 'check-sso',
    //     silentCheckSsoRedirectUri: window.location.origin + '/silent-check-sso.html'
    // })
    // keycloak.init({
    //     onLoad: 'login-required'
    // })
//     console.log(keycloak)
//  return (

//    <div>
//      <div className="top-0 w-full flex flex-wrap">
//        <section className="x-auto">
//        </section>
//      </div>
//    </div>
//  );
// };

// export default Nav;