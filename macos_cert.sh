#!/bin/bash
 
security add-trusted-cert -d -r trustRoot -k \ 
        "/Library/Keychains/System.keychain" \ 
        "/private/tmp/certs/certname.cer"    \
        srm "/private/tmp/certs/certname.cer"