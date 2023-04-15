//es un objeto que representa la culminacion de exito o error de una operacion  asincrona 

import { error, log } from "console";
import { resolve } from "path"

async function ejecucion(){

    console.log ('sumar');
    console.log ('restar');

    const promesa = new Promise((resolve,reject)=>{
        setTimeout(()=> {
            // resolve("informacion guardad en la base de datos ");
            reject(new Error("error al guaradr el regsitro en la base de datos "));
        },5000);
    });

    // promesa
    // .then((respuesta) =>{
    //     console.log(respuesta);
    // });

    // .then((respuesta) =>{
    //     console.log(respuesta);
    // });
    try{
        const respuesta = await promesa;
        console.log(respuesta);
    } catch (error){
        console.error ("error al ejecutar la promesa");
        console .error(error .message);
    }
        console.log("finalizo!");
    }

    ejecucion ();