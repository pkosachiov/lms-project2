# lms-project2

This is a branch of the main Qstore project allocated to a separate repository for the separation of powers and organization of the API and the system administrator part. In the future, it is necessary to attach the API part to the main branch of the Qstore project. This project displays an approximate picture of creating a WhiteList from applications provided from sources such as repositories, flatpack, packages and ansible.

## Scheme

![lms-project2](qstore.drawio.svg)

## White list

The corporate web server acts as an arbitrator. The web server filters POST requests, removing software not from the white list,
the system service on the user's PC executes tasks only from the web server. The identifier is the computer name,
the user name is saved in the request for installing flatpak packages at the user level.

## Screen

![lms-project2](qstore-api.png)
